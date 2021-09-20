nota = float(input("Coloque as suas notas(digite 0 para finalizar): "))
i = 0
n= nota

while nota != 0 :
    nota = float(input("Coloque as suas notas(digite 0 para finalizar): "))
    n += nota
    i +=1 
media = n / i 

if media >= 6 :
    print("Aprovado com média: {} ".format(n))
else:
    print("Reprovado com média: {} ".format(n))
