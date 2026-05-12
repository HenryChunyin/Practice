import re
from pathlib import Path
import xml.etree.ElementTree as ET

path_to_file = "/Users/leichunyin/Desktop/HMM_lecture"
ppt_folder = Path(path_to_file)
slides_folder = ppt_folder / "ppt" / "slides"

ns = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main"
}
slides = sorted(
    slides_folder.glob("slide*.xml"),
    key=lambda p: int(re.search(r"slide(\d+)\.xml", p.name).group(1))
)

for slide_xml in slides:
    tree = ET.parse(slide_xml)
    root = tree.getroot()

    texts = []

    for t in root.findall(".//a:t", ns):
        if t.text:
            texts.append(t.text)

    print(f"\n==== {slide_xml.name} ====")
    print("\n".join(texts))
