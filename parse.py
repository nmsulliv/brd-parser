import xml.etree.ElementTree as ET
import sys

# Check if the filename was passed as an argument
if len(sys.argv) == 1:
    print("*** Please pass in the name of the file you would like to parse. ex: 'python3 parse.py filename.brd'")
    sys.exit()

# Load the board file
tree = ET.parse(sys.argv[1])
# tree = ET.parse("filename.brd") 

root = tree.getroot()


# Get the number of layers
num_layers = len(root.findall(".//layers/layer"))


# Get the board area in millimeters
sides = root.findall(".//board/plain/wire")
xmin = float(sides[0].get('x1'))
xmax = float(sides[-1].get('x1'))
ymin = float(sides[-1].get('y2'))
ymax = float(sides[0].get('y2'))

board_area = (xmax - xmin) * (ymax - ymin)

# Get the chip information
elements_info = root.findall(".//elements/element")
ic_name = ""
for element in elements_info:
    if element.get('name') =="U1":
        ic_name = element.get('value')


# Print the results
print("Number of layers:", num_layers)
print("Board area (mm^2):", board_area) # assuming it's in millimeters, but is it?
print("IC:", ic_name) 

