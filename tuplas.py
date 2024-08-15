# Definindo a primeira tupla
tupla1 = ("Gato", "Cachorro", "Papagaio", "Tartaruga")

# Acessando um elemento da tupla, mesmo formato das listas
print(tupla1[2])

# Sclicing de uma tupla, pegando um intervalo, mesmo que a lista
print(tupla1[1:3])

# Criando uma tupla vazia
tupla_vazia = ()
print(tupla_vazia)

# Não é possível altara um elemento de uma tupla, Phyton retorna um erro
# tupla[1] = "Elefante"

# Para apagar uma tupla, usa-e del(tupla)
# del(tupla1)
# print(tupla1)

# Algumas funções para e usar com tuplas
tupla2 = (8.3, 9.4, 3.3, 7.5, 7.6)
print(max(tupla2))
print(min(tupla2))
print(len(tupla2))

# Transformando uma tupla em lista e vice-versa
lista1 = list(tupla1)
print(lista1)
lista2 = ["José", "Afonso", "Carlos", "Luiz"]
tupla3 = tuple(lista2)
print(tupla3)