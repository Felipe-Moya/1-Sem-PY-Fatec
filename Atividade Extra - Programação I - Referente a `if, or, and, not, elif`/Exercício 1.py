# Reconhecimento de caracteres - Reconhece vogal, consoante e dígito

caracter = input("Digite um caracter: ")

if caracter in "aeiou":
    print("O caracter digitado é vogal.")

elif caracter in "0123456789":
    print ("O caracter digitado é númerico.")

else:
    print ("O caracter digitado é consoante.")