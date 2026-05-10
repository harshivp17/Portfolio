import os

html_file = 'c:/Users/harsh/OneDrive/Desktop/Portfolio/project-destruction.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure we don't duplicate if run multiple times
if 'class="dev-log-slide"' not in content:
    new_content = content.replace('alt="Development Log Slide', 'class="dev-log-slide" alt="Development Log Slide')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Added class successfully.")
else:
    print("Class already exists.")
