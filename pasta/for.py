import random

vereador1 = "João"
proposta_vereador1 = "Investir em educação e saúde"
vereador2 = "Maria"
proposta_vereador2 = "Melhorar o transporte público e a segura"

eleitores = ["Eleitor1", "Eleitor2", "Eleitor3", "Eleitor4", "Eleitor5"]

votos = {}
for eleitor in eleitores:
    voto = random.choice([vereador1, vereador2])
    votos[eleitor] = voto


total_votos_vereador1 = list(votos.values()).count(vereador1)
total_votos_vereador2 = list(votos.values()).count(vereador2)

if total_votos_vereador1 > total_votos_vereador2:
    vencedor = vereador1
else:
    vencedor = vereador2

print(f"Propostas dos vereadores: ")
print(f"{vereador1}: {proposta_vereador1}")
print(f"{vereador2}: {proposta_vereador2}")
print("\nResultados da votação: ")
for eleitor, voto in votos.items():
    print(f"{eleitor} votou em {voto}")
print(f"\nVereador Vencedor: {vencedor}")