import fitz
import os

pdf_path = "assets/Development_Report.pdf"
output_dir = "assets/pdf_slides"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    # Render page to an image. Increase dpi for better quality.
    pix = page.get_pixmap(dpi=150)
    image_path = os.path.join(output_dir, f"slide_{page_num}.png")
    pix.save(image_path)
    print(f"Saved {image_path}")
