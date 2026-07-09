import re

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization\README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Banner
banner_html = '''<div align="center">
  <img src="assets/banner.svg" alt="Awesome Weight Initialization Banner" width="100%">
</div>

'''

# Add Emojis
content = content.replace('# Awesome-Weight-Initialization', '# 🌟 Awesome-Weight-Initialization 🌟')
content = content.replace('## Weight Initialization in AI', '## ⚖️ Weight Initialization in AI')
content = content.replace('## 1. The Macro Chronological Evolution', '## ⏳ 1. The Macro Chronological Evolution')
content = content.replace('## 2. Core Algorithmic & Distribution Variants', '## 🧬 2. Core Algorithmic & Distribution Variants')
content = content.replace('## 3. The Initialization Variance Optimization Matrix', '## 🧮 3. The Initialization Variance Optimization Matrix')
content = content.replace('## 4. Production Engineering Challenges & Cluster Solutions', '## 🏭 4. Production Engineering Challenges & Cluster Solutions')
content = content.replace('## 5. Frontier Real-World AI Industrial Applications', '## 🚀 5. Frontier Real-World AI Industrial Applications')
content = content.replace('## References', '## 📚 References')
content = content.replace('**Follow-Up Options Matrix:**', '🌟 **Follow-Up Options Matrix:**')

if '<img src="assets/banner.svg"' not in content:
    content = banner_html + content

with open(r'C:\Users\ishan\Documents\Projects\Awesome-Weight-Initialization\README.md', 'w', encoding='utf-8') as f:
    f.write(content)
