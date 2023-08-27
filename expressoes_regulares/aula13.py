import re

senha_forte_regexp = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@[-`{-~]).{12,}$',
    flags=re.MULTILINE
)

string = '''
^63&r9R=aBXcn>W5
vUW'7:w5:[J8pgJ5

s50F7WW0m0MsjdaX
9J7ri0lBeWA04Gvw

1"z6@b:r^e%1n53?
z}1]9s_e]8~99)xs

HY35]'_L61Z7{]Y`
>4_94\&ZE3KRL4($

jtmshcrjdzmmczbm
glswktuzxlbzroyo

DPURCJSSLHBIZGZH
DPAMBICEHTOECAHS

7790099637574917
3482314509099678

@(@#>=^{(;{`:|"{
*>|?`_:`:/* +\]^
'''

print(senha_forte_regexp.findall(string))
