import os, re

for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = re.sub(
                r"alert\('Airtable Error: ' \+ \(err\.message \|\| err\)\);",
                r"alert('There was an issue submitting your request. Please try again or contact support.');",
                content
            )

            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Reverted alert in {filepath}")
