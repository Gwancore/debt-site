import glob, re

HERO_SVG = """<!-- Background decoration -->
<div class="absolute top-0 right-0 w-[40rem] h-[40rem] opacity-20 bg-gradient-to-br from-amber-400 to-orange-600 rounded-full mix-blend-multiply filter blur-3xl -translate-y-1/2 translate-x-1/3 pointer-events-none z-0"></div>
<div class="absolute bottom-0 left-0 w-[30rem] h-[30rem] opacity-20 bg-gradient-to-tr from-indigo-500 to-purple-600 rounded-full mix-blend-multiply filter blur-3xl translate-y-1/3 -translate-x-1/4 pointer-events-none z-0"></div>
<svg class="absolute inset-0 w-full h-full pointer-events-none opacity-[0.03] z-0" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <pattern id="dot-pattern" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="1.5" fill="currentColor"></circle>
        </pattern>
    </defs>
    <rect x="0" y="0" width="100%" height="100%" fill="url(#dot-pattern)"></rect>
</svg>
<svg class="absolute right-10 top-20 w-32 h-32 opacity-10 pointer-events-none animate-spin-slow text-amber-500 z-0" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="50" r="48" stroke="currentColor" stroke-width="2" stroke-dasharray="10 10" />
    <path d="M50 10 L90 90 L10 90 Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round" />
</svg>"""

GRAY_SVG = """<!-- Subtle background graphic for light sections -->
<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
    <svg class="absolute -left-20 top-20 w-96 h-96 opacity-5 text-indigo-500 transform rotate-12" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <path fill="currentColor" d="M45.7,-76.3C58.9,-69.3,69,-55.4,77.5,-40.7C86,-26,93.1,-10.5,91.8,4.2C90.5,18.9,80.8,32.7,71.2,46.1C61.6,59.4,52.1,72.4,39.3,79.5C26.5,86.6,10.4,87.8,-4.8,84.9C-20.1,82.1,-34.5,75.1,-48.8,66.8C-63,58.5,-77.2,48.8,-83.4,35.1C-89.6,21.5,-87.8,4,-82.9,-12C-78,-28,-70,-42.6,-58.3,-53.4C-46.6,-64.2,-31.2,-71.4,-16.4,-74.6C-1.5,-77.9,13.1,-77.2,28.2,-79Z" transform="translate(100 100)" />
    </svg>
    <svg class="absolute -right-20 -bottom-20 w-80 h-80 opacity-[0.03] text-amber-500" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <polygon points="50,0 100,25 100,75 50,100 0,75 0,25" fill="currentColor"/>
    </svg>
    <div class="absolute inset-0 bg-[radial-gradient(#cbd5e1_1px,transparent_1px)] [background-size:20px_20px] opacity-[0.15]"></div>
</div>
"""

FOOTER_SVG = """<footer class="relative text-gray-200 py-12 md:py-16 bg-gradient-to-br from-neutral-900 via-neutral-800 to-neutral-900 border-b-4 border-amber-500 text-white shadow-inner overflow-hidden">
<--skip-broken Subtle Footer Background -->
<div class="absolute inset-0 pointer-events-none z-0 overflow-hidden">
    <svg class="absolute top-0 right-0 w-[500px] h-[500px] opacity-10 text-amber-500 transform translate-x-1/3 -translate-y-1/3" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <path fill="none" stroke="currentColor" stroke-width="1.5" d="M10,100 a90,90 0 1,0 180,0 a90,90 0 1,0 -180,0 M30,100 a70,70 0 1,0 140,0 a70,70 0 1,0 -140,0 M50,100 a50,50 0 1,0 100,0 a50,50 0 1,0 -100,0" />
    </svg>
    <div class="absolute bottom-0 left-0 w-full h-1/2 bg-gradient-to-t from-black/20 to-transparent z-0"></div>
</div>
"""

files = glob.glob('*.html') + glob.glob('pages/*.html')

def replacer_gray(match):
    pre = match.group(1)
    classes = match.group(2)
    post = match.group(3)
    if 'relative' not in classes:
        classes = 'relative ' + classes
    if 'overflow-hidden' not in classes:
        classes = classes + ' overflow-hidden'
    return f'<section{pre}class="{classes}"{post}>\n{GRAY_SVG}'

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Apply HERO background
    content = re.sub(
        r'<!-- Background decoration -->\s*<div[^>]*></div>', 
        HERO_SVG, 
        content,
        count=1
    )

    # Apply GRAY background
    content = re.sub(
        r'<section([^>]*)class="([^"]*bg-gray-50[^"]*)"([^>]*)>',
        replacer_gray,
        content
    )
    
    # Apply FOOTER background
    content = re.sub(
        r'<footer\s+class="[^"]*bg-gradient-to-br from-neutral-900[^"]*">',
        FOOTER_SVG,
        content,
        count=1
    )

    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Updated {filepath}")
