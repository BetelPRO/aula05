x, y = 0, 0
for i in range(4):
    num = int(input("Digite um número: "))
    if 10 <= num <= 20:
        x +=1
    else:
        y +=1
print(x,y)