comsumo = float(input("Digíte o consumo do vveículo (km/l):"))
distância = float(input("Dígite a distância percorrida (km):"))

while distância > 0:
    combustível_necessario = distância / comsumo
    print(f"para {distância} você precisará de {combustível_necessario: .2f} litros de combustível.")

    distância = float(input("Dígite uma nova disstância (ou digite 0 para sair):"))
    if distância == 0:
        print("Programa encerrado.")
        break