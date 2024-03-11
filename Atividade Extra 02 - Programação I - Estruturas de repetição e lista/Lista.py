lista = []

while True:
    coisa = input("Digite algo na lista ou aperte (S) para sair: ").lower()

    if coisa == "s":
        print(f"A sua lista contem os seguintes itens {lista}. E contem {len(lista)} itens")
        break
    else:
        lista.append(coisa)
        continue