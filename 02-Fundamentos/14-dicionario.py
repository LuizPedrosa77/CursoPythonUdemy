filmeHarryPotter = {
    "titulo": "Harry Potter",
    "anoLancamento": "2005",
    "classificacaoImdb": "10",
    "genero": ["ficção-científico", "ação"]
}
print(filmeHarryPotter)
print(len(filmeHarryPotter))
print(type(filmeHarryPotter))

# Retorna um elemento o dicionario
print("\n---- Recuperando um elemento o dicionario ----")
print(filmeHarryPotter["anoLancamento"])

# Retorna o resultado do elemento do dicionario
print("\n---- Recuperando o resultado do elemento do dicionario ----")
print(filmeHarryPotter.get("titulo"))

# Retorna apenas as chaves do dicionario
print("\n---- Buscar apenas as chaves do dicionario ----")
print(filmeHarryPotter.keys())

# Retorna apenas os valores do dicionario
print("\n---- Retorna apenas os valores do dicionario ----")
print(filmeHarryPotter.values())

# Retornar itens do dicionario com chave e valor
print("\n---- Retornar itens do dicionario com chave e valor ----")
print(filmeHarryPotter.items())

# Adicionando itens ao dicionario
print("\n---- Adicionando itens ao dicionario ----")
filmeHarryPotter["Diretor"] = "Chris Columbus"
print(filmeHarryPotter)

# Atualizar item do dicionario
print("\n---- Atualizar item do dicionario ----")
filmeHarryPotter.update({"classificacaoImdb": 9.9})
print(filmeHarryPotter.get("classificacaoImdb"))

# Remover item do dicionario
print("\n---- Remover item do dicionario ----")
print(filmeHarryPotter.pop("Diretor"))
print(filmeHarryPotter)
