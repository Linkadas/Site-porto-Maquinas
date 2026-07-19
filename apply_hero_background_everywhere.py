import re

with open('css/index.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Make .content-section exactly the same as .contact-section (the dark hero background)
content_section_pattern = r'\.content-section\s*\{\s*background:\s*#[a-fA-F0-9]+;\s*/\*.*?\*/\s*padding:\s*100px\s*0;\s*\}'
content_section_replacement = """.content-section {
  color: var(--white);
  background-image: linear-gradient(135deg, rgba(17,24,39,0.92) 0%, rgba(31,41,55,0.85) 50%, rgba(163,0,0,0.6) 100%), url(../products/forno-tunel.webp);
  background-position: center;
  background-size: cover;
  background-attachment: fixed;
  padding: 100px 0;
}

.content-section h2, 
.content-section p.eyebrow, 
.content-section .section-head p {
  color: var(--white) !important;
}"""

content = re.sub(content_section_pattern, content_section_replacement, content)

with open('css/index.css', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated CSS to have hero background everywhere.")
