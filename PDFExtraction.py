import fitz
files = "/Users/leichunyin/Documents/In Birmingham/During Study/Modules/5Computational_Biology_for_Complex_System/Lectures/2025-26_mscbioinfor_lecture0.pdf"

doc = fitz.open(files)

'''
for page in doc:
    text = page.get_text().strip()
    print(len(text))
'''

for page_num, page in enumerate(doc, start=1):
    text = page.get_text()
    print(f"--- Page {page_num} ---")
    print(text)
