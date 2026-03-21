import os

script_tag = '<!-- Memberstack webflow package -->\n<script data-memberstackapp="app_cmn04gka7000d0svugewrh0dr" src="https://static.memberstack.com/scripts/v1/memberstack.js" type="text/javascript"></script>'

for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if '</head>' in content and 'data-memberstackapp' not in content:
                content = content.replace('</head>', f'    {script_tag}\n</head>')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Injected Memberstack into {filepath}")
