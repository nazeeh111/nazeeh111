"""Compose the preserved mesh projections; no new geometry or native run.

The original source and required fixture notices stay beside the output.
"""

from copy import deepcopy
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def element(parent, tag, attributes, text=None):
    result = ET.SubElement(parent, f"{{{NS}}}{tag}", attributes)
    result.text = text
    return result


def figure(width, height, name):
    root = ET.Element(f"{{{NS}}}svg", {
        "width": str(width), "height": str(height),
        "viewBox": f"0 0 {width} {height}", "role": "img",
        "aria-labelledby": f"{name}-title {name}-description",
    })
    element(root, "title", {"id": f"{name}-title"},
            "Two input solids; one body missing from Blender's recorded union")
    element(root, "desc", {"id": f"{name}-description"},
            "Both panels show the original 132-triangle case, not the reduced witness. "
            "The left or upper panel contains the two overlapping input solids. "
            "The right or lower panel shows the stored FLOAT union with one body absent.")
    element(root, "style", {}, """/* Hallmark · profile evidence figure · preserved source geometry, responsive comparison */
:root { --ground: #08121d; --ink: #eaf1f6; --muted: #b0c1cf; --line: #304555; --face: Arial, Helvetica, sans-serif; }
.label { fill: var(--ink); font-family: var(--face); font-weight: 600; }
.note { fill: var(--muted); font-family: var(--face); }
""")
    element(root, "rect", {"width": str(width), "height": str(height), "fill": "var(--ground)"})
    return root


source = ET.parse(ROOT / "assets/missing-body-light.svg").getroot()
panels = source.findall(f"{{{NS}}}svg")
if len(panels) != 2:
    raise ValueError("Expected the two preserved original-case projections")

for mobile in (False, True):
    width, height = (640, 740) if mobile else (1000, 370)
    root = figure(width, height, "mobile" if mobile else "comparison")
    for index, (panel, label) in enumerate(zip(panels, ["Two input solids", "Recorded union: one missing"])):
        projected = deepcopy(panel)
        if mobile:
            x, y, w, h = 24, index * 340 + 70, 592, 265
            tx, ty, fs = 28, index * 340 + 44, 31
        else:
            x, y, w, h = index * 500 + 16, 66, 468, 246
            tx, ty, fs = index * 500 + 24, 40, 25
        projected.attrib.update(x=str(x), y=str(y), width=str(w), height=str(h))
        root.append(projected)
        element(root, "text", {"x": str(tx), "y": str(ty), "class": "label", "font-size": str(fs)}, label)
    if not mobile:
        element(root, "path", {"d": "M500 72V306", "stroke": "var(--line)", "stroke-width": "1"})
    element(root, "text", {"x": "28" if mobile else "24", "y": str(height - 24),
                            "class": "note", "font-size": "28" if mobile else "20"},
            "Original 132-triangle case. Stored native output.")
    name = "solidrift-comparison-mobile.svg" if mobile else "solidrift-comparison.svg"
    ET.ElementTree(root).write(ROOT / "assets" / name, encoding="unicode", xml_declaration=False)
