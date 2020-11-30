bignum = 0
arru = {}
position = 0
while position < 100:
    value = int(input())
    if (value > bignum):
        bignum = value
        arru[value] = position
    position += 1
print(bignum)
print(arru[bignum] + 1)