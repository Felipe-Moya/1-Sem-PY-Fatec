#Calcular média

p1 = float(input("Digite a nota da primeira prova: "))
p2 = float(input("Digite a nota da segunda prova: "))
p3 = float(input("Digite a nota da terceira prova: "))
media = (p1 + p2 + p3)/3
if media >= 7:
    print (f"Média: {media:.2f}. Aluno aprovado!")
else:
    print (f"Média: {media:.2f}. Aluno reprovado.")
