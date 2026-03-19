import glob
from bs4 import BeautifulSoup

for filepath in glob.glob("*.html") + glob.glob("pages/*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    menu = soup.find(id="mobile-menu")
    if menu:
        # Instead of breaking layout, safely update Tailwind utility classes.
        # Original: hidden md:hidden bg-gray-50 border-t border-gray-200 px-4 py-4
        
        # We will make it completely cover the screen BELOW the header.
        # Note: the header is sticky top-0, we need the menu to drop down fully.
        new_classes = "hidden md:hidden absolute left-0 w-full bg-white shadow-xl border-b border-gray-200 px-6 py-8 flex flex-col items-center justify-center space-y-6 z-40 transition-all duration-300"
        menu["class"] = new_classes
        
        for a in menu.find_all("a"):
            c = a.get("class", [])
            cc = " ".join(c)
            # Normal links: Make large and centered
            if "nav-link" in cc and "bg-green-500" not in cc:
                a["class"] = "block text-xl font-semibold text-blue-900 hover:text-green-500 py-2"
            # Button link: Keep looking like a button but bigger
            elif "bg-green-500" in cc:
                a["class"] = "block mt-4 w-full bg-green-500 text-white px-6 py-4 rounded-lg font-semibold hover:bg-green-600 transition text-center shadow-md text-xl"
                
    # Update the CSS so block -> flex
    content_str = str(soup)
    content_str = content_str.replace(
        """#menu-toggle:checked ~ #mobile-menu {
            display: block;
        }""",
        """#menu-toggle:checked ~ #mobile-menu {
            display: flex;
            height: 100vh;
        }
        
        /* Change icon from bars to X when checked */
        #menu-toggle:checked ~ nav label .fa-bars:before {
            content: "\\f00d";
        }
        """
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content_str)
