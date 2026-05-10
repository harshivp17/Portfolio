import fitz
import os
import re

pdf_path = "assets/Development_Report.pdf"
output_dir = "assets/extracted_images"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
html_output = ""

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    
    # Get text blocks
    blocks = page.get_text("blocks")
    # Sort blocks by vertical position (y0)
    blocks.sort(key=lambda b: b[1])
    
    # Extract images
    images = page.get_images(full=True)
    saved_images = []
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        img_filename = f"page_{page_num}_img_{img_index}.{image_ext}"
        img_path = os.path.join(output_dir, img_filename)
        with open(img_path, "wb") as f:
            f.write(image_bytes)
        saved_images.append(f"assets/extracted_images/{img_filename}")
    
    # Build HTML for this page
    if not blocks and not saved_images:
        continue # skip empty pages
        
    animation = "animate-slide-left" if page_num % 2 == 0 else "animate-slide-right delay-1"
    panel_class = "comic-panel" if page_num % 2 == 0 else "comic-panel dark-panel"
    heading_color = "var(--accent-yellow)" if page_num % 2 == 0 else "#fff"
    
    panel_html = f'                <div class="{panel_class} {animation}">\n'
    panel_html += f'                    <div class="log-entry">ENTRY {page_num:02d}</div>\n'
    
    text_content = ""
    is_first_block = True
    for b in blocks:
        text = b[4].strip()
        # Clean up text (remove weird bullets, normalize spacing)
        text = text.replace('\u27a2', '▶').replace('\uf0b7', '•').replace('\n', ' ')
        text = re.sub(r'\s+', ' ', text)
        if not text:
            continue
            
        if is_first_block and len(text.split()) < 10:
            # Treat as heading
            panel_html += f'                    <h3 style="color: {heading_color}; margin-bottom: 1rem;">{text}</h3>\n'
            is_first_block = False
        else:
            panel_html += f'                    <p style="margin-bottom: 1rem;">{text}</p>\n'
            is_first_block = False
            
    # Add images
    if saved_images:
        for img_src in saved_images:
            panel_html += f'                    <div class="project-img" style="height: auto; margin-bottom: 1rem; border: 2px solid var(--accent-yellow);">\n'
            panel_html += f'                        <img src="{img_src}" alt="Extracted Image" style="width: 100%;">\n'
            panel_html += f'                    </div>\n'
            
    panel_html += '                </div>\n'
    html_output += panel_html

html_file = "c:/Users/harsh/OneDrive/Desktop/Portfolio/project-destruction.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<div class="log-timeline">'
end_marker = '</section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

new_content = content[:start_idx + len(start_marker)] + "\n" + html_output + "            </div>\n        " + content[end_idx:]

with open(html_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Native HTML generated and injected successfully.")
