#Implemente la selección por orden como un programa: El algoritmo de selección por
#orden acomoda la sucesión s1, . . . , sn en orden no decreciente, para ello encuentra primero
#el elemento más pequeño, por ejemplo si, y lo coloca en el primer lugar intercambiando
#s1 y si. después encuentra el algoritmo más pequeño en s2, . . . , sn, de nuevo digamos si, y
#lo coloca en el segundo lugar intercambiando s2 y si. Continua hasta que la sucesión esté
#ordenada.
def seleccionarOrden(lista,largoLista,contador):
    if contador<largoLista:
        pequeño=lista[contador]
        posicion=contador
        for i in range(contador+1,largoLista):
            if lista[i]<pequeño:
                pequeño=lista[i]
                posicion=i
        lista[contador],lista[posicion]=lista[posicion],lista[contador]
        seleccionarOrden(lista,largoLista,contador+1)
M=[3,6,9,12,4,5,23,9,1]
seleccionarOrden(M,len(M),0)
print(M)