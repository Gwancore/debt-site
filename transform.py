import glob
from bs4 import BeautifulSoup
import re

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    # 1. Add Inter Font from Google Fonts
    head = soup.find("head")
    if head and not head.find("link", href=re.compile("fonts.googleapis.com")):
        font_link1 = soup.new_tag("link", rel="preconnect", href="https://fonts.googleapis.com")
        font_link2 = soup.new_tag("link", rel="preconnect", href="https://fonts.gstatic.com", crossorigin="")
        font_link3 = soup.new_tag("link", rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap")
        head.append(font_link1)
        head.append(font_link2)
        head.append(font_link3)
    
    # 2. Update Body Font Class
    body = soup.find("body")
    if body:
        new_classes = body.get("class", [])
        if "font-sans" in new_classes:
            new_classes.remove("font-sans")
        if "text-gray-800" in new_classes:
            new_classes.remove("text-gray-800")
        if "bg-white" in new_classes:
            new_classes.remove("bg-white")
            
        new_str = " ".join(new_classes) + " font-['Inter'] text-slate-800 bg-slate-50 antialiased"
        body["class"] = new_str

    # 3. Clean up Header (Glassmorphism & Spacing)
    header = soup.find("header")
    if header:
        header["class"] = "sticky top-0 z-50 bg-white/80 backdrop-blur-lg border-b border-slate-200/80 shadow-sm transition-all duration-300"
    
    # 4. Clean up Hero Section (if exists)
    hero = soup.find("section", class_=re.compile("bg-gradient"))
    if hero:
        hero["class"] = "relative bg-gradient-to-tr from-slate-900 via-blue-900 to-indigo-900 text-white py-24 md:py-32 overflow-hidden"

    # 5. Clean up Buttons (Softer shadows, better hover states)
    for btn in soup.find_all("a", class_=re.compile("bg-green-500")):
        classes = btn.get("class", "")
        if isinstance(classes, list): classes = " ".join(classes)
        classes = classes.replace("bg-green-500", "bg-emerald-500").replace("hover:bg-green-600", "hover:bg-emerald-600 hover:shadow-lg hover:shadow-emerald-500/30")
        classes += " ring-1 ring-emerald-500 ring-offset-1 ring-offset-transparent shadow-md"
        btn["class"] = classes.split()
        
    for bg in soup.find_all(class_=re.compile("bg-green-500")):
        classes = bg.get("class", "")
        if isinstance(classes, list): classes = " ".join(classes)
        bg["class"] = classes.replace("bg-green-500", "bg-emerald-500").split()
        
    for text in soup.find_all(class_=re.compile("text-green-500")):
        classes = text.get("class", "")
        if isinstance(classes, list): classes = " ".join(classes)
        text["class"] = classes.replace("text-green-500", "text-emerald-500").split()
        
    for border in soup.find_all(class_=re.compile("border-green-500")):
        classes = border.get("class", "")
        if isinstance(classes, list): classes = " ".join(classes)
        border["class"] = classes.replace("border-green-500", "border-emerald-500").split()

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
