import os

filepath = 'secret-signup.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add the plan ID to the signup form so Memberstack knows what plan they get for free
if 'data-ms-form="signup"' in content and 'data-ms-plan:add=' not in content:
    content = content.replace('<form data-ms-form="signup" class="space-y-4">', '<form data-ms-form="signup" data-ms-plan:add="premium" class="space-y-4">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
