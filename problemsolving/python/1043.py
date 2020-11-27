a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if (a < b + c and b < a + c and c < a + b):
    f1 = a + b + c
    print('Perimetro = %0.1f' % f1)
else:
    f2 = c * (a + b) / 2
    print('Area = %0.1f' % f2)