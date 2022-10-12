
def demandeNombre() :   # demande nombre
        note = input("Entre un nombre ")
        try:
            noteInt = int(note)
        except  ValueError:
            print("erreur Vous devez entre un nombre")
            return demandeNombre()
        return noteInt


nombre = demandeNombre()
for i in range(1,11):
    print(nombre + i)
