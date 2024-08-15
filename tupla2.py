# Criar uma tupla com 5 frutas e imprimindo-a
tupla_frutas = ("Laranja", "Melancia", "Abacaxi", "Melão", "Açai")
print(tupla_frutas)

# Criando uma tupla de 1 a 10, imprimindo o primeiro, terceiro e ultimo elemento
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupla_numeros[0], tupla_numeros[2], tupla_numeros[9])

# Duas tuplas com frutas e cores, depois juntando
tupla_frutas2 = ("Abacaxi", "Laranja", "Melão")
tupla_cores = ("Vermelho", "Rosa", "Amarelo")
print(tupla_cores + tupla_frutas2)

# Tupla com dias da semana e imprimindo o número de elementos
tupla_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo")
print(len(tupla_semana))

# Tupla com 5 países e verifficando se o Brasil está
tupla_país = ("China", "Japão", "Canadá", "Venezuela", "Brasil")
if "Brasil" in tupla_país:
    print("Brasil está na lista")
else:
    print("Brasil não está na lista")

