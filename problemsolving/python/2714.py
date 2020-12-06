# num = int(input())
# while num > 0:
#     num -= 1
#     acadmrecd = input()
#     msg = 'INVALID DATA'
#     if len(acadmrecd) == 20:
#         if acadmrecd[0:20] == 'RA':
#             if acadmrecd[2:].isdigit():
#                 msg = int(acadmrecd[2:])
#     print('acadmrecd')


# num = int(input())
# while num > 0:
#     num -= 1
#     academrecord = input()
#     dinv = 'INVALID DATA'
#     if len(academrecord) == 20:
#         if academrecord[0:2] == 'RA':
#             if academrecord[2:].isdigit():
#                 dinv = int(academrecord[2:])
#     print(dinv)

num = int(input())
while num > 0:
    num -= 1
    academrecord = input()
    dinv = 'INVALID'
    if len(academrecord) == 20:
        if academrecord[0:2] == 'RA':
            if academrecord[2:].isdigit():
                dinv = int(academrecord[2:])
    print(dinv)