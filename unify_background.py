import re

with open('css/index.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update body to include the fixed background layer
body_pattern = r'body\s*\{\s*color:\s*var\(--ink\);\s*background:\s*var\(--paper\);\s*margin:\s*0;\s*font-family:\s*\'Inter\',\s*sans-serif;\s*letter-spacing:\s*-0\.01em;\s*\}'
body_replacement = """body {
  color: var(--white);
  background: var(--ink); /* Fallback */
  margin: 0;
  font-family: 'Inter', sans-serif;
  letter-spacing: -0.01em;
}

/* Hardware-accelerated fixed background for perfect performance and unified look */
body::before {
  content: "";
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
  background-image: linear-gradient(135deg, rgba(17,24,39,0.92) 0%, rgba(31,41,55,0.85) 50%, rgba(163,0,0,0.6) 100%), url(../products/forno-tunel.webp);
  background-position: center;
  background-size: cover;
}"""
content = re.sub(body_pattern, body_replacement, content)

# 2. Make .hero transparent
hero_pattern = r'\.hero\s*\{\s*color:\s*var\(--white\);\s*background-image:.*?;(?:.*?background-size:.*?;)?'
hero_replacement = """.hero {
  color: var(--white);
  background: transparent;"""
# Using regex carefully:
content = re.sub(r'\.hero\s*\{[^}]*align-items:', r'.hero {\n  color: var(--white);\n  background: transparent;\n  align-items:', content)


# 3. Make .content-section transparent
content_section_pattern = r'\.content-section\s*\{\s*color:\s*var\(--white\);\s*background-image:[^}]*padding:\s*100px\s*0;\s*\}'
content_section_replacement = """.content-section {
  color: var(--white);
  background: transparent;
  padding: 100px 0;
}"""
content = re.sub(content_section_pattern, content_section_replacement, content)

# 4. Make .contact-section transparent
contact_section_pattern = r'\.contact-section\s*\{\s*color:\s*var\(--white\);\s*background-image:[^}]*padding:\s*100px\s*0;\s*\}'
contact_section_replacement = """.contact-section {
  color: var(--white);
  background: transparent;
  padding: 100px 0;
}"""
content = re.sub(contact_section_pattern, contact_section_replacement, content)

with open('css/index.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Unified background applied.")
