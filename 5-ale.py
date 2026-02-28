#passo 1: farti dire dall utente qaunti alunni ci sono
#passo 2: farti dire dall utente il nome di ciascun allunno
#passo 3: per ogni alunni di all utente di inserire il voto che ha preso
#passo 4: aggiungi un voto in piu ad ogni alunno
#passo 5: fai la media dei voti di tutta la classe

alunni=[]
voti=[]
n=int(input("dammi numero alunni"))
for i in range (n):
    nome=input("dammi nome di ciascun alunno")
    alunni.append(nome)
    voto=int(input("dammi voto alunni"))
    voto_bonus=voto+1
    voti.append(voto_bonus)
for i in range (len(alunni)):
    print("nome",alunni[i])
    print("voti", voti[i])



