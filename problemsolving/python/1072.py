wt = int(input())

hoy = 0
noy = 0

for i in range(wt):
    value = int(input())
    if (value >= 10 and value <= 20):
        hoy += 1
    else:
        noy += 1
print('%d in' %hoy)
print('%d out'%noy)