import os, re

for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".html") and filename != 'dashboard.html':
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Add login button to mobile menu
            mobile_contact = '<a class="block text-xl font-semibold text-neutral-900 hover:text-amber-500 py-2"\n href="contact.html">Contact</a>'
            mobile_contact_alt2 = '<a class="block text-xl font-semibold text-neutral-900 hover:text-amber-500 py-2\n" href="contact.html">Contact</a>'
            mobile_contact_alt3 = '<a class="block text-xl font-semibold text-neutral-900 hover:text-amber-500 py-2" href="contact.html">Contact</a>'
            login_mobile = '\n<a class="block text-xl font-bold text-amber-600 hover:text-amber-700 py-2" href="#/ms/login" data-ms-modal="login"><i class="fas fa-lock text-sm mr-2"></i>Client Login</a>'
            
            # Use regex for more flexible matching
            pattern = re.compile(r'<a\s+class="block\s+text-xl\s+font-semibold\s+text-neutral-900\s+hover:text-amber-500\s+py-2"\s*href="contact\.html">Contact</a>', re.MULTILINE | re.DOTALL)
            
            if not 'Client Login' in content:
                content = pattern.sub(r'\g<0>' + login_mobile, content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

