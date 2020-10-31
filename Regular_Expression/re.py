# Regular Expression :)

s = 'afganistan, america, Bangladesh, canada, Denmark, England, Greenland, Iceland, Netherland, New Zealand, sweden, switzerland'
countries = s.split(',')
print(countries)
li = [item for item in countries if item.endswith('land')]
print(li)
