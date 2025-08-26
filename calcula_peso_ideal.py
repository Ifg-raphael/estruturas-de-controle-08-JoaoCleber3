altura = float(input("Forneça a altura: "))
sexo = input("Forneça o sexo: (F ou M):")
if sexo == "M":
    peso_ideal = (72.7*altura) - 58
if sexo == "F":
    peso_ideal = (62.1*altura) - 42
print(f"{peso_ideal:.2f}")
