x = 0
for i in range(4):
    num = int(input("Digite um número: "))
    if num < 0:
        x +=1
print(f"Foram digitados {x} números negativos")