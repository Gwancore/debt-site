import glob, re

FOOTER_SVG = """<footer class="relative text-gray-200 py-12 md:py-16 bg-gradient-to-br from-neutral-900 via-neutral-800 to-neutral-900 border-b-4 border-amber-500 text-white shadow-inner overflow-hidden">
<--skip-broken Subtle Footer Background -->
<div class="absolute inset-0 pointer-events-none z-0 overflow-hidden">
    <svg class="absolute top-0 right-0 w-[500px] h-[500px] opacity-10 text-amber-500 transform translate-x-1/3 -translate-y-1/3" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <path fill="none" stroke="currentColor" stroke-width="1.5" d="M10,100 a90,90 0 1,0 180,0 a90,90 0 1,0 -180,0 M30,100 a70,70 0 1,0 140,0 a70,70 0 1,0 -140,0 M50,100 a50,50 0 1,0 100,0 a50,50 0 1,0 -100,0" />
    </svg>
    <div class="absolute bottom-0 left-0 w-full h-1/2 bg-gradient-to-t from-black/20 to-transparent"></div>
</div>
"""

files = glob.glob('*.html') + glob.glob('pages/*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Apply Footer background
    # Looking for:
    # <footer class="text-gray-200 py-12 md:py-16 bg-gradient-to-br from-neutral-900 via-neutral-800 to-neutral-900 border-b-4 border-amber-500 text-white shadow-inner">
    content = re.sub(
        r'<footer\s+class="[^"]*bg-gradient-to-br from-neutral-900[^"]*">',
        FOOTER_SVG,
        content,
        count=1
    )

    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Footer upgraded in {filepath}")
