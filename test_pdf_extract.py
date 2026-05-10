import fitz

pdf_path = "assets/Development_Report.pdf"
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}")
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()
    if "Documentation of Production" in text:
        print(f"Found on page {page_num}")
        print(text)
        break
