meu_dicionario = { 1: "Python", 2: "Java", 3: "PHP" } 

print("Conteúdo do dicionário:",meu_dicionario)
print("Tipo de dados do dicionário:", type(meu_dicionario))
print("O valor da chave 'linguagem':", meu_dicionario.get(1))
print("Tamanho do dicionário:", len(meu_dicionario))

dicionario_frutas = dict({
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
})

print("Conteúdo do dicionário de frutas:", dicionario_frutas)
print("Chave 1 - Nome e tipo:", dicionario_frutas[1]["nome"], dicionario_frutas[1]["tipo"])
print("Chave 2 - Nome e tipo :", dicionario_frutas[2]["nome"], dicionario_frutas[2]["tipo"])
for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave}: Nome = {valor['nome']}, Tipo = {valor['tipo']}")

