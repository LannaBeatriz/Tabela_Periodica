num = int(input("Digite um número: "))
if num > 0: 
    if num %2 == 0:
        print("O númeroné positivo e par.")
    else:
        print("O número é positivo e impar.")
elif num < 0:
    if num %2 == 0:
        print("O número é negativo par.") 
    else:
        print("O número é negativo e impar")
else: 
    print("O número é zero.")