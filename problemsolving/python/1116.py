n = int(input())

for i in range(n):
    x, y = list(map(int,input().split()))
    try:
        print('%.1f' %(x/float(y)))
    except:
        print('divisao impossivel')