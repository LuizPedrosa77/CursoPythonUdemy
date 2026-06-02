linha = '='

'''classe'''


class Jogo:
    '''Metodos da classe'''

    def __init__(self, nome="", anoLancamento=0, multiplayer=0, nota=0):  # Metodo construtor
        '''Atributos'''
        self.nome = nome
        self.anoLancamento = anoLancamento
        self. multiplayer = multiplayer
        self.nota = nota
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


class JogoStudio:
    def __init__(self, nome=""):
        self.nome = nome
        self.jogos = []

    def addJogo(self, jogo):
        self.jogos.append(jogo)

    def avaliacaoQualidadeStudio(self):
        totalNotas = sum(jogo.nota for jogo in self.jogos)
        numJogos = len(self.jogos)
        if numJogos == 0:
            print(f"O estúdio {self.nome} ainda não lançou nenhum jogo")
        else:
            mediaNota = totalNotas / numJogos
            print(
                f"Avaliação média dos jogos do estúdio {self.nome}: {mediaNota:.2f}")


jogo1 = Jogo("CSGO", 2020, True, 8.5)
jogo2 = Jogo("FortNite", 2020, True, 8)
jogo3 = Jogo("EuroTruck", 2010, False, 8.5)

studio = JogoStudio("Incrível")
studio.addJogo(jogo1)
studio.addJogo(jogo2)
studio.addJogo(jogo3)

studio.avaliacaoQualidadeStudio()

for jogo in studio.jogos:
    jogo.fichaTecnica()
