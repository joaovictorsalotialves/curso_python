# Meta caracteres:  ^ $ ( )

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
'''

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))
