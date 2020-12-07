# n = int(input())
# cou = 0
# indur = 0
# bang = 0
# khorgosh = 0

# for i in range(n):
#     amount, typ = input().split()
#     str(typ)
#     cou +=int(amount)
#     if typ == 'C':
#         khorgosh += int(amount)
#     elif typ == 'R':
#         indur += int(amount)
#     elif typ == 'S':
#         bang += int(amount)
# print('Total: %d cobaias' %cou)
# print('Total de khorgoshs: %d' %khorgosh)
# print('Total de indurs: %d' %indur)
# print('Total de bangs: %d' %bang)
# print('Percentual de khorgoshs: %.2f' %float(((100*khorgosh)/cou)),'%')
# print('Percentual de indurs: %.2f' %float(((100*indur)/cou)),'%')
# print('Percentual de bangs: %.2f' %float(((100*indur)/cou)),'%')
#5% wrong


n=int(input())
cont,indur,bang,khorgos=0,0,0,0
for i in range(n):
    Quantia,Tipo=input().split()
    str(Tipo)
    cont+=int(Quantia)
    if Tipo== 'C':
        khorgos +=int(Quantia)
    elif Tipo=='R':
        indur+=int(Quantia)
    elif Tipo=='S':
        bang+=int(Quantia)

print('Total: %d cobaias' %cont)
print('Total de khorgoss: %d' %khorgos)
print('Total de indurs: %d' %indur)
print('Total de bangs: %d' %bang)
print('Percentual de khorgoss: %.2f' %float(((100*khorgos)/cont)),'%')
print('Percentual de indurs: %.2f' %float(((100*indur)/cont)),'%')
print('Percentual de bangs: %.2f' %float(((100*bang)/cont)),'%')