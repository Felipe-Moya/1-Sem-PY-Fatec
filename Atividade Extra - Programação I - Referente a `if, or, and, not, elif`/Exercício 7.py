# conversor de temperatura

med = input("Digite 'C' para Celsius ou 'F' para Fahrenheit: ")

if med == "C" or med == "c":
    temp1 = float(input("Digite a temperatura em Celsius: "))
    conv1 = (temp1 * (9 / 5)) + 32
    print(f"{temp1}°C é igual a {conv1:.1f}°F")

elif med == "F" or med == "f":
    temp2 = float(input("Digite a temperatura em Fahrenheit: "))
    conv2 = (temp2 - 32) * 5/9
    print(f"{temp2}°F é igual a {conv2:.1f}°C")

else:
    print("Caracter inválido. Reinicie o programa e digite C ou F.")