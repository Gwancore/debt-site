import glob

files = glob.glob("*.html") + glob.glob("pages/*.html")

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Fix missing plus in the url data attributes that my sed command stripped incorrectly
    content = content.replace('"telephone": "27614490671"', '"telephone": "+27614490671"')
    content = content.replace('tel:27614490671', 'tel:+27614490671')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
