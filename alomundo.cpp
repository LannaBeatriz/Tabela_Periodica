temperatura = float(input("Digite a temperatura atual em graus Celsius: "))

if temperatura >= 30:
    print("Que tal pegar uma praia?")
elif 20 <= temperatura < 30:
    print("Que tal passear no parque?")
elif 10 <= temperatura < 20:
    print("Que tal assistir a um filme com pipoca em casa?")
else:
    print("Que tal ficar em casa e aproveitar um bom livro?")
    