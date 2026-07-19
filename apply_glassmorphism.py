import re

with open('css/index.css', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .catalog-panel and children for dark glassmorphism
old_catalog_css = r'\.catalog-panel \{ background: var\(--white\); color: var\(--ink\); border-radius: var\(--radius-lg\); padding: 40px; box-shadow: var\(--shadow-md\); \}\n\.catalog-panel-head \{ display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 32px; \}\n\.catalog-panel-head h3 \{ font-size: 28px; font-weight: 800; margin: 0 0 8px; \}\n\.search-field \{ display: flex; flex-direction: column; gap: 8px; font-size: 13px; font-weight: 700; color: var\(--muted\); text-transform: uppercase; \}\n\.search-field input \{ border: 1px solid var\(--line\); border-radius: var\(--radius-sm\); padding: 12px 16px; background: var\(--paper\); transition: var\(--transition\); \}\n\.search-field input:focus \{ background: var\(--white\); border-color: var\(--red\); box-shadow: 0 0 0 3px rgba\(220, 38, 38, 0\.1\); outline: none; \}\n\.catalog-meta \{ display: grid; grid-template-columns: repeat\(2, 1fr\); gap: 16px; margin-bottom: 32px; \}\n\.catalog-meta div \{ background: var\(--paper\); border-left: 4px solid var\(--red\); padding: 16px; border-radius: 0 var\(--radius-sm\) var\(--radius-sm\) 0; \}\n\.catalog-meta strong \{ display: block; font-weight: 700; margin-bottom: 4px; text-transform: uppercase; font-size: 14px; color: var\(--ink\); \}\n\.catalog-meta span \{ color: var\(--steel\); font-size: 13px; font-weight: 500; \}'

new_catalog_css = """.catalog-panel { 
  background: rgba(31, 41, 55, 0.4); 
  backdrop-filter: blur(20px); 
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: var(--white); 
  border-radius: var(--radius-lg); 
  padding: 40px; 
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.3); 
}
.catalog-panel-head { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 32px; }
.catalog-panel-head h3 { font-size: 28px; font-weight: 800; margin: 0 0 8px; color: var(--white); }
.catalog-panel-head p { color: #d1d5db; margin: 0; }
.search-field { display: flex; flex-direction: column; gap: 8px; font-size: 13px; font-weight: 700; color: #d1d5db; text-transform: uppercase; }
.search-field input { border: 1px solid rgba(255, 255, 255, 0.15); border-radius: var(--radius-sm); padding: 12px 16px; background: rgba(0, 0, 0, 0.2); color: var(--white); transition: var(--transition); }
.search-field input::placeholder { color: rgba(255, 255, 255, 0.4); }
.search-field input:focus { background: rgba(0, 0, 0, 0.4); border-color: var(--red); box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.2); outline: none; }
.catalog-meta { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 32px; }
.catalog-meta div { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.05); border-left: 4px solid var(--red); padding: 16px; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; }
.catalog-meta strong { display: block; font-weight: 700; margin-bottom: 4px; text-transform: uppercase; font-size: 14px; color: var(--white); }
.catalog-meta span { color: #9ca3af; font-size: 13px; font-weight: 500; }"""

if re.search(old_catalog_css, content):
    content = re.sub(old_catalog_css, new_catalog_css, content)
    with open('css/index.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully transformed catalog-panel to glassmorphism.")
else:
    print("Regex failed to match. Try checking the file contents.")
