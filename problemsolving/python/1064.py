
# cnt = 0
# sum = 0.0
# for i in range(1,7):
#     n = float(input())
#     if (n > 0 ):
#         sum = sum + n
#         cnt = cnt + 1
# print('{} valores positivos'.format(cnt))
# print('%0.1f'%(sum/cnt))

cnt=0
sum=0.0
for i in range(1,7):
    n = float(input())
    if(n>0):
        sum = sum + n
        cnt=cnt+1
print("{} valores positivos".format(cnt))
print("%0.1f"%(sum/cnt))

# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())
# f = float(input())
# positive = [a, b, c, d, e, f]
# count = 0
# for item in positive:
#     if item > 0:
#         count += 1
# # print(f"{count} valores positivos")
# print('{} valores positivos'.format(count))

# total = sum(x for x in positive if x > 0)
# print(total/count)