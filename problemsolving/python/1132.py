n1 = int(input())
n2 = int(input())
tor = n1
sm = 0
if (n1 > n2):
    n1 = n2
    n2 = tor

while (n1 <= n2):
    if (n1%13 != 0):
        sm += n1
    n1 += 1
print(sm)