import docx
import os

doc_path = "c:/Users/harsh/OneDrive/Desktop/Portfolio/assets/temp_ldd.docx"
html_file = "c:/Users/harsh/OneDrive/Desktop/Portfolio/project-racing.html"
# Map image names from XML to our extraction path
media_dir = "assets/trackmania_media/word/media"

try:
    doc = docx.Document(doc_path)
except Exception as e:
    print(f"Error loading docx: {e}")
    exit(1)

# Major headings to split panels
major_headings = ["High Level Overview", "Map Overview", "Challenges & Obstacles", "Mission & Narrative"]
current_panel_index = -1
panels_content = ["", "", "", ""]

# We'll also track specific headings for image placement
image_map = {
    "Top down-level layout": ["image1.png", "image2.png"],
    "Car change blocks": ["image3.png", "image4.png", "image5.png", "image6.png"],
    "Start / Finish line": ["image7.png"]
}

for para in doc.paragraphs:
    text = para.text.strip()
    if not text or text == "LEVEL DESIGN DOCUMENTATION TRACKMANIA LEVEL":
        continue
        
    if text in major_headings:
        current_panel_index = major_headings.index(text)
        panels_content[current_panel_index] += f'                    <h3 style="color: var(--accent-yellow); margin-bottom: 1rem; font-size: 2rem;">{text}</h3>\n'
    elif current_panel_index >= 0:
        if len(text.split()) < 6:
            panels_content[current_panel_index] += f'                    <h4 style="color: #fff; margin-bottom: 0.5rem; margin-top: 1.5rem; font-size: 1.2rem;">{text}</h4>\n'
            # Check if this heading needs images
            if text in image_map:
                for img in image_map[text]:
                    panels_content[current_panel_index] += f'                    <div class="project-img" style="height: auto; margin-top: 1rem; margin-bottom: 1rem; border: 2px solid var(--accent-yellow);">\n'
                    panels_content[current_panel_index] += f'                        <img src="{media_dir}/{img}" alt="{text}" style="width: 100%;">\n'
                    panels_content[current_panel_index] += f'                    </div>\n'
        else:
            panels_content[current_panel_index] += f'                    <p style="margin-bottom: 1rem;">{text}</p>\n'

html_output = ""
for i, content in enumerate(panels_content):
    if not content: continue
    
    animation = "animate-slide-left" if i % 2 == 0 else "animate-slide-right delay-1"
    panel_class = "comic-panel" if i % 2 == 0 else "comic-panel dark-panel"
    
    panel_html = f'                <div class="{panel_class} {animation}">\n'
    panel_html += f'                    <div class="log-entry">ENTRY {i+1:02d}</div>\n'
    panel_html += content
    panel_html += '                </div>\n'
    html_output += panel_html

with open(html_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Reconstruct HTML, replacing the old log section
new_lines = []
skip = False
for line in lines:
    if '<section class="report-section">' in line:
        skip = True
        new_lines.append(f"""
        <section class="report-section">
            <h2 class="section-title">LEVEL DESIGN LOG</h2>
            <div class="log-timeline">
{html_output}
            </div>
        </section>
""")
    if not skip:
        new_lines.append(line)
    if skip and '</section>' in line:
        # Check if it's the end of the report-section
        # (Assuming the log-timeline section was the last thing added)
        skip = False

with open(html_file, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("HTML successfully updated with contextual images in project-racing.html")
