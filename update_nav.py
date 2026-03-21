import os, re

for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".html") and filename != 'dashboard.html':
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add Login button to desktop nav
            if 'href="contact.html">Contact</a>' in content and 'data-ms-modal="login"' not in content:
                content = content.replace(
                    '<a class="nav-link" href="contact.html">Contact</a>',
                    '<a class="nav-link" href="contact.html">Contact</a>\n<a class="nav-link font-semibold text-amber-600 hover:text-amber-700" href="#/ms/login" data-ms-modal="login">Login <i class="fas fa-lock text-xs ml-1"></i></a>'
                )
            
            # Update the main CTA to be a "Sign Up" button. Let's just find "Free Assessment" CTA and add a login button, or update contact buttons.
            # Actually, let's just make the changes safely without breaking styling. We'll add a signup button next to the secondary mobile buttons etc if needed. 
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated nav in {filepath}")
