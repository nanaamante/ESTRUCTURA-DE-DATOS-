#Implemente el siguiente algoritmo como un programa para desordenar.
import random
def desordenar(lista, largoLista,contador):
    if contador<largoLista:
        numeroRandom=random.randint(contador,largoLista-1)
        lista[contador],lista[numeroRandom]=lista[numeroRandom],lista[contador]
        desordenar(lista,largoLista,contador+1)
M=[2,4,6,8,10,12,14]
desordenar(M,len(M),0)
print(M)
