# Ano bissexto

ano = float(input("Digite um ano: "))

if (ano/4).is_integer() and (not (ano/100).is_integer()):
    print("O ano é bissexto.")

elif (ano/400).is_integer():
    print ("O ano é bissexto.")

else:
    print("O ano não é bissexto.")