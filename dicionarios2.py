dicionarios2 = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
        }

novos_elementos = {
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'brasileira'},
    4: {'nome': 'Carlos', 'idade': 28, 'nacionalidade': 'argentino'}
}

dicionarios2.update(novos_elementos)
print(dicionarios2)
dicionarios2_copia = dicionarios2.copy()
dicionarios2.pop(2)
print(dicionarios2)
dicionarios2.popitem()
print(dicionarios2)
dicionarios2.clear()
print(dicionarios2)
dicionarios2_copia.clear()
print(dicionarios2_copia)

letras = {'a', 'e', 'i', 'o', 'u'}
valor = 'vogal'
vogais = dict.fromkeys(letras, valor)

print(vogais.items())
print(vogais.keys())
print(vogais.values())

