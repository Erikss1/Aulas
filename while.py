x = 0
while x < 5:
    print(f'O valor de x é {x} ')
    x += 1

print()

y = 0
while y < 10:
    print(y)
    if y == 5:
        print("Parando o loop com break")
        break
    y += 1

print()

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

print()

b = 0
while b < 5:
    b += 1
    print(b)
else:
    print("O comando oi finalizado com sucesso")

print()