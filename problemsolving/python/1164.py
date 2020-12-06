ipt = int(input())
for q in range(ipt):
    n = int(input())
    sm = 0
    for i in range(1, n):
        if (n % i == 0):
            sm += i
    if (sm == n):
        print('%d eh perfeito' %n)
    else:
        print('%d nao eh perfeito' %n)