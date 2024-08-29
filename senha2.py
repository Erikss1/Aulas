senha_correta = "1234"
tentativa = input("Digite a sua senha:")
numero_tentativas = 0

while tentativa != senha_correta:
    numero_tentativas += 1

    if numero_tentativas == 3:
        print("Limite de tentativas esgotadas. Tente mais tarde")
        break

    print("Senha incorreta. Tente novamente")
    tentativa = input("Digite a sua senha:")

else:
    print("Senha correta. Acesso concedido")