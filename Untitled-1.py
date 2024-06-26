def receber_dados_temperatura():
    dados_temperatura = float(input("digite a temperatura atual: "))
    return dados_temperatura

def processar_dados(dados):
    print('dados de temperatura recebidos e processados: ', dados)

def verificar_sinal_desligamento():
    if dados_temperatura > 90:
        print("Temperatura muito alta. o progama sera encerrado")
        return True
    else:
        return False

sinal_desligamento = False

while not sinal_desligamento:
    dados_temperatura = receber_dados_temperatura()
    processar_dados(dados_temperatura)
    sinal_desligamento = verificar_sinal_desligamento()