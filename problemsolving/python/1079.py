n = int(input())

for i in range(n):
    n2 = list(map(float,input().split()))
    a, b, c = n2
    a = a * 2
    b = b * 3
    c = c * 5
    avg = (a + b + c) / 10
    print('%.1f' %avg)