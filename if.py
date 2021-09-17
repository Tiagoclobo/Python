media = int(input("Digite sua média: "))

if media <= 29:
    print("Reprovado.")
elif media <= 49:
    print("Recuperação")
else:
    print("Aprovado.")