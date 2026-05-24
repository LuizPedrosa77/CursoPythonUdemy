import pprint

filmesDicionario = {
    "harryPotter": {
        "anoLancamento": 2006,
        "notaImdb": 9.5,
        "genero": ["ficção-cietifico", "acao"],
    },
    "interestrelar": {
        "anoLancamento": 2014,
        "notaImdb": 8.6,
        "genero": ["ficção-cietifico", "drama"],
    },
    "devoradorDeEstrela": {
        "anoLancamento": 2026,
        "notaImdb": 8.5,
        "genero": ["ficção-cietifico", "drama", 'futurista']
    }
}
print("\n---- Imprimindo de forma mais bonita ----")
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmesDicionario)

# Buscar uma informação dentro de um dicionario aninhado
print("\n---- Buscar uma informação dentro de um dicionario aninhado ----")
print(filmesDicionario["interestrelar"]["genero"])

# Adicionando item "Diretor"
print("\n---- Adicionando item 'Diretor' ----")
filmesDicionario["devoradorDeEstrela"]["Diretor"] = "Christopher Miller"
print(filmesDicionario["devoradorDeEstrela"])

# Excluir um dicionario
print("\n---- Excluir um dicionario ----")
del filmesDicionario["harryPotter"]
pp.pprint(filmesDicionario)
