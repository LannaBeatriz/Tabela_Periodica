def switvh_dia(dia):
    dias= {
        1: "segunda",
        2: "terça",
        3: "quarta",
        4: "quinta",
        5: "sexta",
        6: "sabado",
        7: "domingo",
    }
    return dias.get(dia, "dia invalido")

dia_selecionado= switvh_dia(int(input("digite seu dia:")))
print("o dia é:", dia_selecionado)

    
    