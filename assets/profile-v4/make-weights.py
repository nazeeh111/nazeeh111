"""Extract the 48 illustrated weight prisms from the generated model view."""
from pathlib import Path
import xml.etree.ElementTree as ET
root = ET.parse('model.svg').getroot()
polygons = root.findall('{http://www.w3.org/2000/svg}polygon')
assert len(polygons) == 48 * 3
shapes = ''.join(ET.tostring(p, encoding='unicode').replace('ns0:', '').replace('xmlns:ns0="http://www.w3.org/2000/svg"', '') for p in polygons)
colors = {'#779bff':'#7390ff','#244fe2':'#2756df','#1436ab':'#173bb0','#6d8196':'#a2a2a2','#354b60':'#535353','#101820':'#202020','#d6dfeb':'#e1e1e1','#bdcbda':'#a7a7a7','#f6f8fb':'#ffffff'}
for source, target in colors.items():
    shapes = shapes.replace(source, target)
Path('weights.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="30 105 715 280">' + shapes + '</svg>')
