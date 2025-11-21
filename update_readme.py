import random

# Load quotes
with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

# Choose one at random and format it for centered markdown
random_quote = random.choice(quotes)
new_quote_block = f'<div align="center">\n\n> *{random_quote.lower()}*\n\n</div>'

# Load README
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Replace content between the markers
start_marker = "<!-- quote-start -->"
end_marker = "<!-- quote-end -->"
in_block = False
new_lines = []

for line in lines:
    if start_marker in line:
        in_block = True
        new_lines.append(line)
        new_lines.append(new_quote_block + "\n")
        continue
    if end_marker in line:
        in_block = False
        new_lines.append(line)
        continue
    if not in_block:
        new_lines.append(line)

# Save updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
