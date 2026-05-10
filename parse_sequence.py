import xml.etree.ElementTree as ET
import os

xml_path = "c:/Users/harsh/OneDrive/Desktop/Portfolio/assets/temp_unzipped/word/document.xml"
rel_path = "c:/Users/harsh/OneDrive/Desktop/Portfolio/assets/temp_unzipped/word/_rels/document.xml.rels"

# Map rId to image filename
namespaces = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture'
}

# Read relationships
rels = {}
tree_rels = ET.parse(rel_path)
root_rels = tree_rels.getroot()
for child in root_rels:
    rId = child.attrib.get('Id')
    target = child.attrib.get('Target')
    if 'media/' in target:
        rels[rId] = target.replace('media/', '')

# Read document structure
tree = ET.parse(xml_path)
root = tree.getroot()

sequence = []
for p in root.findall('.//w:p', namespaces):
    text = "".join([t.text for t in p.findall('.//w:t', namespaces) if t.text])
    if text:
        sequence.append(("text", text))
    
    # Check for drawings in this paragraph
    for drawing in p.findall('.//w:drawing', namespaces):
        for blip in drawing.findall('.//a:blip', namespaces):
            embed_id = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
            if embed_id in rels:
                sequence.append(("image", rels[embed_id]))

for item_type, content in sequence:
    print(f"{item_type.upper()}: {content[:100]}...")
