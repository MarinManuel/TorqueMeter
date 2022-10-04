# Torque Meter
A low-cost, Open-Source device to evaluate hypertonia in a rabbit model of cerebral palsy
![A 3D model of the finished device](https://github.com/MarinManuel/TorqueMeter/blob/7ad48c22c7a120d471c87918b3fdc1228bf73fee/Assets/Figure%201.png)

## Files
 - Schematics.fzz - Schematics of the electronics, Fritzing format
 - Schematics.svg - svg export of the above
 - enclosure.svg - file for laser cutter
 - Torque Meter 3D Model.FCStd - CAD files for the hardware.
                                 FreeCAD v.0.20 format
 - 3D print/ - folder containing the STL files for 3D printing the hardware
               components. Exported from the file above
 - Assets/ - contains datasheets and other misc. Files
 - ArduinoTorqueMeter/ - the main Arduino Sketch
 - CalibTorqueMeter/ - Arduino sketch for calibrating the load cell output
 - TorquePlotter/ - Python software for capturing and plotting data from the
                    Torque Meter

## LICENSES
Copyright Preston Steel, Marin Manuel 2022
### Hardware
This source describes Open Hardware and is licensed under the CERN-OHL-S v2.You may redistribute and modify this source and make products using it under the terms of the CERN-OHL-S v2 (https://ohwr.org/cern_ohl_s_v2.txt).This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE. Please see the CERN-OHL-S v2 for applicable conditions.
As per CERN-OHL-S v2 section 4, should You produce hardware based on this source, You must where practicable maintain the Source Location visible on the external case of the Gizmo or other products you make using this source.
## Software         
The Torque Meter software is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

The Torque Meter software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with the Torque Meter software. If not, see <https://www.gnu.org/licenses/>.
