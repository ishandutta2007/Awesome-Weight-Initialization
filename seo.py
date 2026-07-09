import re

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization\README.md', 'r', encoding='utf-8') as f:
    content = f.read()

badges_left = '''<p align="center">
  <a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a>
  <a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
</p>

> **A comprehensive, SEO-optimized curated list of awesome weight initialization strategies, methodologies, and scaling tricks for deep learning neural networks. Improve model convergence, stabilize training, and solve vanishing/exploding gradients in modern AI.**

'''

content = content.replace('# 🌟 Awesome-Weight-Initialization 🌟\n', '# 🌟 Awesome-Weight-Initialization 🌟\n' + badges_left)

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization\README.md', 'w', encoding='utf-8') as f:
    f.write(content)
