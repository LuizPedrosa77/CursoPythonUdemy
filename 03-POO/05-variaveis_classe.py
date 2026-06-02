linha = '='

'''classe'''


class Jogo:
    '''Variavel da classe'''
    totalJogos = 0
    '''Metodos da classe'''

    def __init__(self, nome="", anoLancamento=0, multiplayer=0, nota=0):  # Metodo construtor
        '''Atributos'''
        self.nome = nome
        self.anoLancamento = anoLancamento
        self. multiplayer = multiplayer
        self.nota = nota
        Jogo.totalJogos += 1
        self.totalAvaliacao = 0
        self.avaliadores = 0

    def __str__(self):
        return f"Jogo: {self.nome}"

    def fichaTecnica(self):
        print(linha * 50)
        print("##### Dados do jogo #####")
        print(f"Nome do jogo: {self.nome}")
        print(f"O ano de lançamento: {self.anoLancamento}")
        print(f"Modo multiplayer: {self.multiplayer}")
        print(f"A avaliação do jogo é: {self.nota}")

    def avaliacao(self, nota):
        self.totalAvaliacao += nota
        self.avaliadores += 1

    def media(self):
        print(
            f"A média do jogo: {self.nome}: {self.totalAvaliacao / self.avaliadores}")


jogo1 = Jogo("CSGO", 2020, True, 8.5)
jogo2 = Jogo("FortNite", 2020, True, 8)

jogo1.fichaTecnica()
jogo1.avaliacao(9.0)
jogo1.avaliacao(8.5)
jogo1.media()

jogo2.fichaTecnica()
jogo2.avaliacao(9.5)
jogo2.avaliacao(9.0)
jogo2.media()


# Exibindo total de jogos criados
print(f"Exibindo total e jogos criados: {Jogo.totalJogos}")
