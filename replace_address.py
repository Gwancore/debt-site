import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # JSON LD 
    content = content.replace('"streetAddress": "123 Business Plaza",', '"streetAddress": "144 Oxford Road, Rosebank",')
    content = content.replace('"addressLocality": "London",', '"addressLocality": "Johannesburg",')
    content = content.replace('"addressRegion": "England",', '"addressRegion": "Gauteng",')
    content = content.replace('"postalCode": "SW1A 1AA",', '"postalCode": "2196",')
    content = content.replace('"addressCountry": "GB"', '"addressCountry": "ZA"')
    
    # footer
    content = content.replace('123 Business Plaza<br/>London, UK<br/>SW1A 1AA', '144 Oxford Road, Rosebank<br/>Johannesburg, 2196<br/>South Africa')
    content = content.replace('123 Business Plaza<br>London, UK<br>SW1A 1AA', '144 Oxford Road, Rosebank<br>Johannesburg, 2196<br>South Africa')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done replacing.")
