class Usuario:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha

    def alterar_senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("A nova senha não atende aos critérios de segurança.")

    def get_nome(self):
        return self.__nome

    def get_senha(self):
        return self.__senha

usuario1 = Usuario("fulano", "senhaAntiga7855")
print("Nome de usuario: fulano")
print("Senha atual:", usuario1.get_senha())
usuario1.alterar_senha("nova")
usuario1.alterar_senha("novaSenhaSegura7564")
print("Nova senha:", usuario1.get_senha())
