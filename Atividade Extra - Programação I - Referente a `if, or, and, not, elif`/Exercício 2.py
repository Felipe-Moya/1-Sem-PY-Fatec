# Indica se um número é divisível por 3 e 5

número = float(input("Digite um número:"))

if (número/3).is_integer() and (número/5).is_integer():
    print(f"É divisível por 3 e 5")
else:
    print(f"Não é divisível por 3 e 5.")