senha_correta = "1234"
tentativa = input("Digite a sua senha:")

while tentativa != senha_correta:
    print("Senha incorreta. Tente novamente")
    tentativa = input("Digite a sua senha:")

    if tentativa != senha_correta:
        print("Senha incorreta. Tente novamente")
        tentativa = input("Digite a sua senha:")

    if tentativa != senha_correta:
        print("Bloqueado por muitas tentativas")
        print("Tente novamente mais tarde")
        break

else:
    print("Senha correta. Acesso concedido")