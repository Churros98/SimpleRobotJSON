# SimpleRobotJSON

SimpleRobotJSON is a Fusion 360 Python script that generate a JSON description of a simple robot from joints in the active Fusion 360 document. It is designed to be dropped into Fusion 360's Scripts folder and run from the Scripts and Add-Ins dialog.

## Features
- Create a compact JSON robot description
- Create simple joint relationships between each component
- Intended for small kinematic prototypes and learning Fusion 360 API basics

## Requirements
- Autodesk Fusion 360 (latest or recent build)
- Fusion 360 Python API (installed as part of Fusion)

## Installation
1. Copy the repository folder (SimpleRobotJSON) to:
    MacOS: `~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts/`
    Windows: `C:\Users\<YourUsername>\AppData\Local\Autodesk\Autodesk Fusion 360\API\Scripts\`

2. Open Fusion 360 → Scripts and Add-Ins → My Scripts, select SimpleRobotJSON and Run.

## Usage
- Run the script from Fusion 360. The script will create components and joints in the active design.
- Use the generated json with "unrobot" library.

## Troubleshooting
- Script doesn't appear: ensure folder is under the Fusion 360 Scripts path and that manifest/entry files exist.

## Contributing
- Open issues or pull requests with improvements, JSON schema refinements, or additional joint types.
- Keep changes small and focused.

## License
- MIT