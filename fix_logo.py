import os
import glob

files = glob.glob('*.html') + glob.glob('js/*.js')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    content = content.replace('porto-maquinas-logo.png', 'porto-maquinas-logo.webp')
    
    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed logo extension in {filepath}")

print("Done fixing logo extensions")
