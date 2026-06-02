linha = '='

'''classe'''

# Classe Pai (Super classe) ou generalista


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

# Classe derivada (subclasse) ou especializada


class jogoParaUmJogador(Jogo):
    def __init__(self, nome="", anoLancamento=0, nota=0, enredo=""):
        super().__init__(nome, anoLancamento, multiplayer=False, nota=nota)
        self.enredo = enredo

    def fichaTecnica(self):
        super().fichaTecnica()
        print(f"O enredo: {self.enredo}")


multJogo = Jogo("Fortnite, 2017, True, 9")
multJogo.fichaTecnica()

jogadorUnico = jogoParaUmJogador(
    "PUBG", 2010, 8.5, "Jogo de mundo aberto de tiro e ação")
jogadorUnico.fichaTecnica()
