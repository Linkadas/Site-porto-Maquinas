import os
import re
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = re.sub(r'main\.js(["\'])', r'main.js?v=2\1', content)
    new_content = re.sub(r'main\.js\?v=\d+(["\'])', r'main.js?v=2\1', new_content)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated JS cache in {file}")
