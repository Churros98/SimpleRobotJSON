""" Simple Robot JSON
Generate robot descriptor and saves it in a JSON file.
"""

import traceback
import adsk.core
import adsk.fusion
import json

app = adsk.core.Application.get()
ui = app.userInterface

def get_rotation_axis(joint_motion):
    joint_motion = adsk.fusion.RevoluteJointMotion.cast(joint_motion)

    if joint_motion.rotationAxis == adsk.fusion.JointDirections.XAxisJointDirection:
        return (1, 0, 0)
    elif joint_motion.rotationAxis == adsk.fusion.JointDirections.YAxisJointDirection:
        return (0, 1, 0)
    elif joint_motion.rotationAxis == adsk.fusion.JointDirections.ZAxisJointDirection:
        return (0, 0, 1)
    else:
        return (0, 0, 0)

def create_header(data: dict):
    data['name'] = app.activeDocument.name
    data['version'] = app.activeDocument.version
    data['author'] = app.activeDocument.attributes.itemByName('Design', 'Author').value if app.activeDocument.attributes.itemByName('Design', 'Author') else 'Unknown'
    data['description'] = f'Fusion 360 robot descriptor generated with SimpleJointsYAML'

def run(_context: str):
    try:
        data = {}
        create_header(data)

        # Get the active design
        des = adsk.fusion.Design.cast(app.activeProduct)
        if not des:
            ui.messageBox('No active Fusion design', 'Error')
            return
    
        base_link = None

        # Find the root compoment called "base_link"
        for component in des.allComponents:
            if component.name == "base_link":
                app.log(f'Component found: {component.name} with id {component.id}')
                base_link = component
                break

        if not base_link:
            ui.messageBox('No component named "base_link" found in the design.', 'Error')
            return

        app.log(f'Base link id: {base_link.id}')

        joints_desc = {}
        joints = des.rootComponent.allJoints
        app.log(f'Total joints found: {len(joints)}')

        # Create all joints
        id = 0
        for joint in joints:
            occ1 = joint.occurrenceOne
            occ2 = joint.occurrenceTwo

            if occ1 is None:
                app.log(f'Joint {joint.name} has no occurrenceOne!')

            to_part = f'{occ1.name.replace(":", "")}'  if occ1 else None
            from_part = f'{occ2.name.replace(":", "")}' if occ2 else None

            if occ2 is None:
                app.log(f'Joint {joint.name} is not connected to any component. (End Joint?)')
            else:
                app.log(f'Joint {joint.name} connects {from_part} to {to_part}')

            if joints_desc.get(from_part):
                joints_desc[from_part]["linked_to"].append( str(to_part) )
            else:                
                joints_desc[from_part] = {
                    "id": int(id),
                    "is_root" : bool(occ2.component.id == base_link.id),
                    "origin": {
                        "x": float(joint.geometryOrOriginOne.origin.x),
                        "y": float(joint.geometryOrOriginOne.origin.y),
                        "z": float(joint.geometryOrOriginOne.origin.z)
                    },
                    "linked_to": [ str(to_part) ]
                }

                if joint.jointMotion.jointType == adsk.fusion.JointTypes.RevoluteJointType:
                    joints_desc[from_part]["rotation"] = get_rotation_axis(joint.jointMotion)
                    joints_desc[from_part]["constraint"] = {
                        "min": adsk.fusion.RevoluteJointMotion.cast(joint.jointMotion).rotationLimits.minimumValue * (180.0 / 3.141592653589793),
                        "max": adsk.fusion.RevoluteJointMotion.cast(joint.jointMotion).rotationLimits.maximumValue * (180.0 / 3.141592653589793)
                    }
                else:
                    app.log(f'WARNING: Joint {joint.name} - unsupported joint type {joint.jointMotion.jointType}')

            app.log(f'Processed joint: {joint.name}')
            id += 1

        data['joints'] = joints_desc

        # Show save file dialog and save JSON
        joints_json = json.dumps(data, indent=4)

        save_dialog = ui.createFileDialog()
        save_dialog.isMultiSelectEnabled = False
        save_dialog.title = 'Save Robot JSON'
        save_dialog.filter = 'JSON files (*.json)'
        dialog_result = save_dialog.showSave()
        if dialog_result == adsk.core.DialogResults.DialogOK:
            file_name = save_dialog.filename
            with open(file_name, 'w') as json_file:
                json_file.write(joints_json)

            ui.messageBox(f'Robot descriptor successfully generated', 'Simple Robot JSON')
    except Exception as e:
        ui.messageBox(f'Failed:\n{traceback.format_exc()}')
