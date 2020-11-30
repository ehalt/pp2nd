x,y=list(map(int,input().split()))
if(x == 1):
    price  = (float) (4.00 * y)
elif(x == 2):
    price  = (float) (4.50 * y)
elif(x == 3):
    price  = (float) (5.00 * y)
elif (x == 4):
    price  = (float) (2.00 * y);
elif (x == 5):
    price  = (float) (1.50 * y)
print("Total: R$ %.2f"%price)