sm = 0
ip = 0
while ip < 2:
    note = float(input())
    if(note >= 0 and note <= 10):
        sm += note
        ip += 1
    else:
        print("nota invalida")

print("media = %.2f" %(sm/2))