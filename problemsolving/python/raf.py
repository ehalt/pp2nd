# N1, N2, N3, N4 = map(float, input().split())

# average = (((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10)

# print("Media: %0.1lf" %average)

# if average >= 7.0:
#     print("Aluno aprovado.")
# elif average < 5.0:
#     print("Aluno reprovado.")
# # elif 5.0 >= average <= 6.9:
# elif average >=5.0 and average <= 6.9:
#     print("Aluno em exame.")
#     n = float(input())
#     print('Nota do exame: %.1lf'%n)
#     avarage2 = (average + n) / 2
#     if avarage2 >= 5.0:
#         print('Aluno aprovado.')
#     if avarage2 <= 4.9:
#         print('Aluno reprovado.')
#     print('Media final: %.1lf'%avarage2)

# N1, N2, N3, N4 =list(map(float, input().split()))

# average = (((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10)

# print("Media: %0.1f" % average)

# if average >= 7.0:
#     print("Aluno aprovado.")
# elif average < 5.0:
#     print("Aluno reprovado.")
# elif 5.0 <= average <= 6.9:
#     print("Aluno em exame.")
#     n = float(input())
#     print("Nota do exame: %0.1f" % n)
#     average2 = (average + n) / 2
#     if average2 >= 5.0:
#         print('Aluno aprovado.')
#     if average2 <= 4.9:
#         print('Aluno reprovado.')
#     print("Media final: %0.1f" % average2)

N1,N2,N3,N4 = input().split(" ")

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

average = float(((N12)+(N23)+(N34)+(N41))/(2+3+4+1))

print("Media: %.1f"%average)

if(average>=7.0):
    print("Aluno aprovado.")
elif average<5.0:
    print("Aluno reprovado.")
elif average>=5.0 and average<7.0:
    print("Aluno em exame.")
    N5 = float(input())
    print("Nota do exame: %.1f"%N5)
    average = (average+N5)/2

    if(average>= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado")
    print("Media final: %.1f"%average)