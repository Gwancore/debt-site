import os

old_block = """                submitBtn.disabled = true;
                btnText.textContent = 'Submitting...';

                submitTimeout = setTimeout(() => {
                    form.style.display = 'none';
                    successMsg.classList.remove('hidden');
                    form.reset();
                    fields.forEach(f => f.classList.remove('error'));

                    resetTimeout = setTimeout(() => {
                        form.style.display = 'block';
                        successMsg.classList.add('hidden');
                        submitBtn.disabled = false;
                        btnText.textContent = 'Submit Your Debt for Free Assessment';
                    }, CONFIG.FORM_RESET_DELAY);
                }, CONFIG.FORM_SUBMIT_DELAY);"""

new_block = """                submitBtn.disabled = true;
                btnText.textContent = 'Submitting...';

                const formData = new FormData(form);
                const data = Object.fromEntries(formData.entries());

                fetch('/api/submit-lead', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        companyName: data['company-name'],
                        email: data['email'],
                        debtAmount: data['debt-amount'],
                        message: data['message'] || ''
                    })
                })
                .then(res => res.json())
                .then(response => {
                    form.style.display = 'none';
                    successMsg.classList.remove('hidden');
                    form.reset();
                    fields.forEach(f => f.classList.remove('error'));

                    resetTimeout = setTimeout(() => {
                        form.style.display = 'block';
                        successMsg.classList.add('hidden');
                        submitBtn.disabled = false;
                        btnText.textContent = 'Submit Your Debt for Free Assessment';
                    }, CONFIG.FORM_RESET_DELAY);
                })
                .catch(err => {
                    console.error('Error:', err);
                    alert('There was an issue submitting your request.');
                    submitBtn.disabled = false;
                    btnText.textContent = 'Submit Your Debt for Free Assessment';
                });"""

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
                print(f"Updated {filepath}")
