num = int(input("Digite um número: "))
if num > 0:
    for i in range(1, num + 1):
        print(i, end=" ")
else:
    for i in range(0, num -1, -1):
        print(i, end=" ")
