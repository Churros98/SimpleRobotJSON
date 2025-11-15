# SimpleRobotJSON

SimpleRobotJSON is a Fusion 360 Python script that generate a JSON description of a simple robot from joints in the active Fusion 360 document. It is designed to be dropped into Fusion 360's Scripts folder and run from the Scripts and Add-Ins dialog.

The description can be used with [unrobot](https://github.com/Churros98/unrobot) library.

## Features
- Create a compact JSON robot description
- Create simple joint relationships between each component
- Intended for small kinematic prototypes and learning Fusion 360 API basics

## Requirements
- Autodesk Fusion 360 (latest or recent build)
- Fusion 360 Python API (installed as part of Fusion)

## Installation
1. Copy the repository folder (SimpleRobotJSON) to:
    1. MacOS: `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts/`
    2. Windows: `C:\Users\<YourUsername>\AppData\Local\Autodesk\Autodesk Fusion 360\API\Scripts\`

2. Open Fusion 360 → Scripts and Add-Ins → My Scripts, select SimpleRobotJSON and Run.

## Usage
- Create your robot using Assembly, add constraints, and set this position in "sleep" mode.
- The base component of the robot (the root) need to be called "base_link".
- Run the script from Fusion 360. The script a description from components and joints in the active design.
- Use the generated json with [unrobot](https://github.com/Churros98/unrobot) library.

## Troubleshooting
- Script doesn't appear: ensure folder is under the Fusion 360 Scripts path and that manifest/entry files exist.

## Contributing
- Open issues or pull requests with improvements, JSON schema refinements, or additional joint types.
- Keep changes small and focused.

## License
- MIT