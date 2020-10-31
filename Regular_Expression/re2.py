import re

s = 'afganistan, america, Bangladesh, canada, Denmark, England, Greenland, Iceland, Netherland, New Zealand, sweden, switzerland'
li = re.findall(r'(w+land*)',s)
print(li)