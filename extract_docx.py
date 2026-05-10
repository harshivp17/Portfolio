import docx
import os
import zipfile

doc_path = "c:/Users/harsh/OneDrive/Desktop/Portfolio/assets/temp_ldd.docx"
output_media_dir = "c:/Users/harsh/OneDrive/Desktop/Portfolio/assets/trackmania_media"

print("--- TEXT PREVIEW ---")
try:
    doc = docx.Document(doc_path)
    for i, para in enumerate(doc.paragraphs):
        if para.text.strip():
            print(f"[{i}] {para.text.strip()}")
except Exception as e:
    print(f"Error reading with docx: {e}")

print("\n--- EXTRACTING IMAGES ---")
os.makedirs(output_media_dir, exist_ok=True)
try:
    with zipfile.ZipFile(doc_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.startswith('word/media/'):
                zip_ref.extract(file, output_media_dir)
                print(f"Extracted: {file}")
except Exception as e:
    print(f"Error unzipping: {e}")

print("\nScript completed.")
