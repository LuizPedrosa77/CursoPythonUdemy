linha = '='

'''classe'''


class Jogo:
    nome = ""
    anoLancamento = 0
    multiplayer = 0
    nota = 0.0


'''Instanciando a classe'''
# Primeiro jogo
jogo1 = Jogo()
jogo1.nome = "CSGO"
jogo1.anoLancamento = 2020
jogo1.multiplayer = True
jogo1.nota = 10

print("##### Dados do jogo 1 #####")
print(
    f"Nome do jogo 1 é: {jogo1.nome} e seu ano de lançamento é: {jogo1.anoLancamento}")

print(linha * 50)

'''Instanciando a classe'''
# Seguno Jogo
jogo2 = Jogo()
jogo2.nome = "PUBG"
jogo2.anoLancamento = 2015
jogo2.multiplayer = True
jogo2.nota = 8

print("##### Dados do jogo 2 #####")
print(
    f"Nome do jogo 1 é: {jogo2.nome} e seu ano de lançamento é: {jogo2.anoLancamento}")

print(linha * 50)

'''Instanciando a classe'''
# Terceiro Jogo
jogo3 = Jogo()
jogo3.nome = "Fortnite"
jogo3.anoLancamento = 2017
jogo3.multiplayer = True
jogo3.nota = 9

print("##### Dados do jogo 3 #####")
print(
    f"Nome do jogo 1 é: {jogo3.nome} e seu ano de lançamento é: {jogo3.anoLancamento}")
