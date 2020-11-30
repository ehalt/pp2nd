a,b,c = list(map(float,input().split()))

d = b * b - 4 * a * c
e = pow(d, .5)
if (d < 0 or a == 0):
    print('Impossivel calcular')
else:
    ful = (-b + e) / (2 * a)
    gul = (-b - e) / (2 * a)
    print('R1 = %.5lf'%ful)
    print('R2 = %.5lf'%gul)
