
def lista_disp():
    return [1, 2]


scrittura_su_chiavetta = True
while True:

    if scrittura_su_chiavetta:
        x = open("prova.txt", "w")
        for j in range(100):
            x.write("Ciao " + str(j))
        x.close()
        scrittura_su_chiavetta = False
    else:
        y = lista_disp()
        if y:  # chiavetta e copia
            x.copy()
            x.delete()
            scrittura_su_chiavetta = True
        else:  # non chiavetta e non copia
            x = open("prova.txt", "r+")
            for j in range(100):
                x.write("Ciao" + str(j))
            scrittura_su_chiavetta = False
            x.close()
