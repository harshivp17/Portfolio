import os

output_html = ""

for i in range(33):
    animation = "animate-slide-left" if i % 2 == 0 else "animate-slide-right delay-1"
    panel_class = "comic-panel" if i % 2 == 0 else "comic-panel dark-panel"
    
    # We'll just put a generic text, since the slide itself has the content.
    entry = f"""
                <div class="{panel_class} {animation}">
                    <div class="log-entry">ENTRY {i:02d}</div>
                    <div class="project-img" style="height: auto; margin-bottom: 1rem;">
                        <img src="assets/pdf_slides/slide_{i}.png" alt="Development Log Slide {i}" style="width: 100%; border: 2px solid #000;">
                    </div>
                </div>
"""
    output_html += entry

html_file = "c:/Users/harsh/OneDrive/Desktop/Portfolio/project-destruction.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<div class="log-timeline">'
end_marker = '</section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

new_content = content[:start_idx + len(start_marker)] + output_html + "            </div>\n        " + content[end_idx:]

with open(html_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("HTML updated!")
