exemplo = [1, 2, 3, 5]
if 3 in exemplo:
    index = exemplo.index(3)
    exemplo[index] = 33
print(exemplo)

# Exercício 1
numero = [1, 2, 3, 4, 5, 6, 99, 8, 9, 10]
if 7 in numero:
    index = numero.index(7)
    numero[index] = numero.remove
else:
    numero.append(7)
print(numero)

# Exercício 2
fruta = ["maçã", "banana", "laranja"]
if "uva" in fruta:
    print("uva está na lista")
else:
    fruta.append("uva")
print(fruta)

# Exercício 3
lista = [2, 88, 9, 7]
if lista[0] % 2 == 0:
    index = lista.index(lista[0])
    lista[index] = lista[0]*2
else:
    index = lista.index(lista[0])
    lista[index] = lista[0] * 0.5
print(lista)
