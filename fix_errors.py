import os

old_block = """                .then(res => res.json())
                .then(response => {"""

new_block = """                .then(async res => {
                    const response = await res.json();
                    if (!res.ok || response.error) throw new Error(response.error || 'Server error');
                    return response;
                })
                .then(response => {"""

for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if old_block in content:
                content = content.replace(old_block, new_block)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

