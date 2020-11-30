tore, pidamu = list(map(int,(input().split())))
if (tore < pidamu):
    somoy = pidamu - tore
else:
    somoy = pidamu + 24 - tore
print('O JOGO DUROU {} HORA(S)'.format(somoy))