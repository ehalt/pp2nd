clmn = int(input())
oper = input()
sm = 0

for i in range(144):
    value = float(input())
    if (i == clmn):
        sm += value
        clmn += 12
if (oper == 'S'):
    print('%.1f' %sm)
else:
    print('%.1f' %(sm / 12.0))