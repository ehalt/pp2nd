

# st,sm,et,em=list(map(int,input().split()))
# ft = et - st;
# if(ft < 0):
#     ft = 24 + (et - st)
# fm = em - sm
# if(fm < 0):
#      fm = 60 + (em - sm)
#      ft=ft-1
# if (et == st and em == sm):
#     print("O JOGO DUROU 24 HORA(S) E 0 ininitminnNUTO(S)")
# else:
#     print("O JOGO DUROU {} HORA(S) E {} ininitminnNUTO(S)".format(ft,fm))

hi,initmin,finalhr,finalmin=map(int, input().split())
if (finalhr-hi==1) and (initmin>finalmin):
    a=60-initmin
    m= a+finalmin
    h=0
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
elif (hi==finalhr)and (initmin==finalmin):
    h=24
    m=0
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
elif (hi<finalhr) and (initmin<finalmin):
    h= finalhr-hi
    m=finalmin-initmin
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
elif (hi<finalhr)and(initmin>finalmin):
    h= (finalhr-hi)-1
    a= 60-initmin
    m=a+finalmin
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
elif (hi==finalhr)and(initmin<finalmin):
    h=0
    m=finalmin-initmin
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
elif (hi>finalhr):
    h=(24-hi)+finalhr
    m=finalmin-initmin
    if (initmin>finalmin):
        h=h-1
        m=(60-initmin)+finalmin
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))
    else:
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(h,m))








