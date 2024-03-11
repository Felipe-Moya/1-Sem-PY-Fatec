# classifica triângulo

lado1 = int(input("Digite o número do primeiro lado: "))
lado2 = int(input("Digite o número do segundo lado: "))
lado3 = int(input("Digite o número do terceiro lado: "))

if lado1 == lado2 == lado3:
    print ("O triângulo é equilátero.")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print ("O triângulo é isósceles.")

else:
    print ("O triângulo é escaleno")