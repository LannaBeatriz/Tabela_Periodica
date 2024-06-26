produto = input("fale a categoria do produto:  ").lower()
Quantidade = int(input("E quantos itens o cliente comprou:  "))
if produto == "tecnologia":
    if Quantidade >= 2:
        print("Parabens, você recebeu 10% de desconto!.")
    else:
        print("O cliente não tem direito a desconto!")
elif produto == "vestuario":
    if Quantidade >= 3:
        print("Você ganhou 20% de desconto.") 
    else:
        print("O Cliente não tem direito a desconto!")
else:
    print("O Cliente não tem direito a desconto!")
