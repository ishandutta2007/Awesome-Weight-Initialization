import re

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization\README.md', 'r', encoding='utf-8') as f:
    content = f.read()

follower_badge = '  <a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>\n</p>'

content = content.replace('</p>', follower_badge, 1)

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization\README.md', 'w', encoding='utf-8') as f:
    f.write(content)
