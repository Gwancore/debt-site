import os, re

for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".html") and filename != 'dashboard.html':
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add login button to mobile menu
            mobile_contact = '<a class="block text-xl font-semibold text-neutral-900 hover:text-amber-500 \npy-2" href="contact.html">Contact</a>'
            mobile_contact_alt = '<a class="block text-xl font-semibold text-neutral-900 hover:text-amber-500 py-2" href="contact.html">Contact</a>'
            login_mobile = '\n<a class="block text-xl font-bold text-amber-600 hover:text-amber-700 py-2" href="#/ms/login" data-ms-modal="login"><i class="fas fa-lock text-sm mr-2"></i>Client Login</a>'
            
            if mobile_contact in content and 'Client Login' not in content:
                content = content.replace(mobile_contact, mobile_contact + login_mobile)
            elif mobile_contact_alt in content and 'Client Login' not in content:
                content = content.replace(mobile_contact_alt, mobile_contact_alt + login_mobile)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

