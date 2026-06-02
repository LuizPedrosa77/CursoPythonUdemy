linha = '='

'''classe'''


class Jogo:
    '''Metodos da classe'''

    def __init__(self, nome="", anoLancamento=0, multiplayer=0, nota=0):  # Metodo construtor
        self.nome = nome
        self.anoLancamento = anoLancamento
        self. multiplayer = multiplayer
        self.nota = nota

    def __str__(self):
        return f"Jogo: {self.nome}"


jogo1 = Jogo("CSGO", 2020, True, 8.5)
jogo2 = Jogo("FortNite", 2020, True, 8)


print("##### Dados do jogo 1 #####")
print(
    f"Nome do jogo 1 é: {jogo1.nome} e seu ano de lançamento é: {jogo1.anoLancamento}")

print(linha * 50)

print("##### Dados do jogo 2 #####")
print(
    f"Nome do jogo 1 é: {jogo2.nome} e seu ano de lançamento é: {jogo2.anoLancamento}")
