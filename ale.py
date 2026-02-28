
nome=[]
cognome=[]
maglia=[]
num=5
for i in range (num):
    name=input("dammi name ciascun giocatore")
    nome.append(name)
    surname=input("dammi cognome ciascun giocatore")
    cognome.append(surname)
    shirt=input("dammi maglia ciascun giocatore")
    maglia.append(shirt)
for i in range (len(maglia)):
    print("nome", nome[i])
    print("cognome", cognome[i])
    print("maglia", maglia[i])

