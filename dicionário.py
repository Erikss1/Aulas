dados = {"nome": "Robert D. Jr.", "idade": 900}
if "cidade" in dados:
    dados["cidade"] = "Rio de Janeiro"
else:
    dados["cidade"] = "São Paulo"
print(dados)

# Exercício 1
dados2 = {"produto": "refrigerante", "preço": 20}
if "desconto" in dados2:
    print(oi)
else:
    dados2["desconto"] = 10
print(dados2)

# Exercício 2
dados3 = {"Nome": "Érik", "Idade": 14}
if dados3["Idade"] >= 18:
    dados3["+18"] = True
else:
    dados3["+18"] = False
print(dados3)

# Exercício 3
dados4 = {"a": 1, "b": 2, "c": 3, "d": 4}
if "d" in dados4:
    print("d está no dicionário")
else:
    dados4["d"] = 4
    print("d foi adicionado ao dicionário")
