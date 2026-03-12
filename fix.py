import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update font link
content = content.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
)
content = content.replace(
    'Google Fonts: Playfair Display, Manrope',
    'Google Fonts: Inter'
)

# 2. Update font CSS variables
content = content.replace("--font-body: 'Manrope', sans-serif;", "--font-body: 'Inter', sans-serif;")
content = content.replace("--font-display: 'Playfair Display', serif;", "--font-display: 'Inter', sans-serif;")

# 3. Add transition to * element globally
transition_orig = '''        :focus-visible {
            outline: 3px solid var(--accent-cyan);
            outline-offset: 2px;
            border-radius: 4px;
        }'''
transition_new = '''        :focus-visible {
            outline: 3px solid var(--accent-cyan);
            outline-offset: 2px;
            border-radius: 4px;
        }

        *, *::before, *::after {
            transition: background-color 0.3s ease, background 0.3s ease, color 0.3s ease, border-color 0.3s ease, fill 0.3s ease;
        }'''
content = content.replace(transition_orig, transition_new)

# 4. Fix colors in :root Light mode
root_light_orig = '''            /* Light mode (default) */
            --bg-primary: #003366;
            --bg-secondary: #004080;
            --text-primary: #ffffff;
            --text-secondary: #E0E0E0;
            --card-bg: #004080;
            --border-color: #005599;'''

root_light_new = '''            /* Light mode (default) */
            --bg-primary: #f6f8fb;
            --bg-secondary: #eef2f7;
            --text-primary: #0f1b2d;
            --text-secondary: #4a5b6d;
            --card-bg: #ffffff;
            --border-color: #d4dde8;'''

content = content.replace(root_light_orig, root_light_new)

# 5. Fix colors in body.dark-mode
dark_mode_pattern = re.compile(r'body\.dark-mode\s*\{[^}]+\}', re.DOTALL)
dark_mode_new = '''body.dark-mode {
            --primary: #3b82f6;
            --primary-light: #60a5fa;
            --primary-dark: #2563eb;
            --bg-primary: #0f1b2d;
            --bg-secondary: #1a2a44;
            --text-primary: #f6f8fb;
            --text-secondary: #a0aec0;
            --card-bg: #16263f;
            --border-color: #2d3e59;
            --shadow-sm: 0 1px 4px rgba(0, 0, 0, 0.3);
            --shadow-md: 0 6px 18px rgba(0, 0, 0, 0.4);
            --shadow-lg: 0 14px 32px rgba(0, 0, 0, 0.5);
            --focus-ring: rgba(59, 130, 246, 0.4);
        }'''
content = re.sub(dark_mode_pattern, dark_mode_new, content)

# 6. Fix btn-secondary
btn_sec_orig = '''        .btn-secondary {
            background: var(--neutral-white);
            color: var(--primary);
            border: 2px solid var(--primary);
        }'''
btn_sec_new = '''        .btn-secondary {
            background: var(--card-bg);
            color: var(--primary);
            border: 2px solid var(--primary);
        }'''
content = content.replace(btn_sec_orig, btn_sec_new)

# 7. Remove dark mode overrides block
overrides_pattern = re.compile(r'\s*/\*\s*Dark mode readability overrides\s*\*/.*?/\*\s*Responsive\s*\*/', re.DOTALL)
content = re.sub(overrides_pattern, '\\n        /* Responsive */', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Replacements done!')
