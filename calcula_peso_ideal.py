altura = float(input())
sexo = input()
if sexo == "M":
    peso_ideal = (72.7*altura) - 58
else:
    peso_ideal = (62.1*altura) - 44.7
print(f"{peso_ideal:.2f}")
