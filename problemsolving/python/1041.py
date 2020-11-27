x,y=list(map(float,input().split()))
x,y = input().split()
x = float(x)
y = float(y)
if(x==0 and y==0):
    print("Origem")
elif(x==0):
    print("Eixo y")
elif(y==0):
    print("Eixo x")
elif(x>0 and y>0):
    print("Q1")
elif(x<0 and y>0):
    print("Q2")
elif(x<0 and y<0):
    print("Q3")
elif(x>0 and y<0):
    print("Q4")