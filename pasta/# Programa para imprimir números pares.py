# Programa para imprimir números pares até um limite fornecido pelo usuário usando for

# Recebe o limite máximo do usuário
limite = int(input("Digite o limite máximo para os números pares: "))

# Itera usando um laço for para imprimir números pares até o limite
print("Números pares até", limite, ":")

for num in range(2, limite + 1, 2):
    print(num)
