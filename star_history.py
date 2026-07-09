import re

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization\README.md', 'r', encoding='utf-8') as f:
    content = f.read()

star_history = '''
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Weight-Initialization&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Weight-Initialization&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Weight-Initialization&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Weight-Initialization&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''

content += star_history

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization\README.md', 'w', encoding='utf-8') as f:
    f.write(content)
