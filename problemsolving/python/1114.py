# pas = int(input())
# if pas == 2002:
#     print('Acesso Permitido')
# else:
#     print('Senha Invalida')

# while (True):
#     a = int(input())
#     if (a == 2002):
#         print('Acesso Permitido')
#         break
#     else:
#         print('Senha Invalida')
#         break

while(True):
    try:
        a = int(input())
        if(a==2002):
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")
    except EOFError:
        break