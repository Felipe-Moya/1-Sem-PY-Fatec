senha = "1234"
cont = 0
tentativas = 2
while True:
    senha_d = input("Digite sua senha: ")
    if senha_d == senha:
        print("Senha correta.")
        break
    elif senha_d != senha and cont < 2:
        print(f"Senha incorreta, mais {tentativas} tentativas")
        cont += 1
        tentativas -= 1
    else:
        print("Muitas tentativas.")
        break
