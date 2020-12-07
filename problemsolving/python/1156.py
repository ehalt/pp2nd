s = 1
temp = 2
count = 3
while(count < 40):
    s += float(count)/float(temp)
    temp *= 2
    count += 2
print('%.2f'%s)

# x = 1
# sum = 0
# for i in range(1, 40, 2):
#     divide = i / x
#     x = x * 2
#     sum += divide
# print("%0.2f" % sum)