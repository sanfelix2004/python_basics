# ESERCIZIO 3
# Scopo: leggere un voto e dire se lo studente è promosso o bocciato.

voto = int(input("Inserisci il voto (0-10): "))

# if controlla una condizione
if voto >= 6:
    # questo blocco viene eseguito solo se la condizione è vera
    print("Promosso")
else:
    # questo blocco viene eseguito se la condizione è falsa
    print("Bocciato")