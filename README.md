⚙️ Gear Generator
An engineering tool designed for the rapid creation of high-precision involute gear profiles. This application provides a bridge between geometry theory and physical manufacturing, allowing users to generate ready-to-use vector geometry for various CAD and CAM workflows.

Project Overview
The Gear Generator automates the process of creating accurate gear teeth for mechanical projects. Unlike simplified circular approximations, this tool calculates the exact path of the tooth profile based on the fundamental principles of gearing. This ensures that the generated gears provide smooth motion transfer and proper meshing when used in mechanical assemblies.

Key Capabilities
Vector Export: Support for DXF (AutoCAD/Fusion 360) and SVG (Laser Cutting/Inkscape).

CAD Optimization: Generates "Closed LWPolylines" in DXF format, allowing for immediate extrusion operations without the need to repair or close the sketch manually.

Real-time Analysis: Interactive interface that displays critical engineering dimensions such as Pitch, Outer, and Root diameters as parameters are adjusted.

Multi-Language UI: A fully localized experience supporting over 15 international languages.

Installation & Setup
Prerequisites
The tool requires Python 3.x and the following dependencies:

Bash

pip install matplotlib ezdxf numpy
Usage
Run the script:

Bash

python "generator zembatek.py"
Adjust the Module, Number of Teeth, and Pressure Angle.

Specify the Shaft Hole diameter if a central mounting point is required.

Export the design using the DXF or SVG buttons.

Manufacturing Workflow
For 3D Printing
Export the profile as a DXF.

Import the file into a CAD environment.

Extrude the profile to the desired thickness and export as an STL or 3MF for slicing.

For Laser or Waterjet Cutting
Export the profile as an SVG.

Open the file in the machine's CAM software.

The paths are optimized as continuous vector lines for clean and efficient cutting.
