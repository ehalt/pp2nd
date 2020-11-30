# n1 = input().split()
# n2 = input().split()
# n3 = input().split()
# n4 = input().split()

# n1 = float(n1)
# n2 = float(n2)
# n3 = float(n3)
# n4 = float(n4)

# n = float(input())

# avarage = (n1 + n2 + n3 + n4) / 2

# avarage2 = (avarage + n ) / 2

# if avarage < 5.0:
#     print('Media: %0.1f'%avarage)
#     print('Aluno reprovado.')
# elif avarage >= 7.0:
#     print('Media: %0.1f'%avarage)
#     print('Aluno aprovado.')
# elif avarage >= 5.0 and avarage < 6.10:
#     print('Media: %0.1f'%avarage)
#     print('Aluno em exame.')
# elif:
#     print('')

# N1, N2, N3, N4 = map(float, input().split())
# n = float(input())
# average = (N1 + N2 + N3 + N4) / 4
# average2 = (average + n) / 2

# if average < 5.0:
#     print("Media: %0.1f" % average)
#     print("Aluno reprovado")
# elif average >= 7.0:
#     print("Media: %0.0f" % average)
#     print("Aluno aprovado")
# elif 5.0 <= average <= 6.9:
#     print("Media: %0.1f" % average)
#     print("Aluno em exame.")
# elif average2 >= 5.0:
#     print("Nota do exame: %0.1f" % n)
#     print("Aluno aprovado")
#     print("Media final: %0.1f" % average2)
# elif average2 <= 4.9:
#     print("Nota do exame: %0.1f" % n)
#     print("Aluno reprovado")
#     print("Media final: %0.1f" % average2)

n1,n2,n3,n4=list(map(float,input().split()))
avarage = (((n1*2)+(n2*3)+(n3*4)+(n4*1))/10)
print('Media: %.1f'%avarage)
if avarage >= 7.0:
    print('Aluno aprovado.')
elif avarage < 5.0:
    print('Aluno reprovado.')
elif avarage >= 5.0 and avarage <= 6.9:
    print('Aluno em exame.')
    new = float(input())
    print('Nota do exame: %.1f'%new)
    av2 = (avarage + new) / 2
    if av2 >= 5.0:
        print('Aluno aprovado.')
    if av2 <= 4.9:
        print('Aluno reprovado.')
    print('Media final: %.1f'%av2)


