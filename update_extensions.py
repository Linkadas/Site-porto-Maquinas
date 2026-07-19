import os
import glob

# Files to process
files = glob.glob('*.html') + glob.glob('js/*.js')

# Replacements
for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We only want to replace image references in the products directory
    # The references look like: "./products/07-fb-500-e.jpg"
    # To be safe, we will just replace .jpg and .webp IF they are preceded by /products/ or similar.
    # Actually, let's just do a simple replace since this is a simple static site and we know we only have products images.
    
    original_content = content
    content = content.replace('.jpg', '.png').replace('.jpeg', '.png').replace('.webp', '.png')
    
    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated {filepath}")

print("Done updating file extensions to .png")
