#Corra el algoritmo anterior “desordena” (del ejercicio 1) muchas veces para la mismasucesión de entrada. ¿Como puede analizarse la salida para determinar si esverdaderamente “aleatorio”?
import random
def desordenar(lista, largoLista,contador):
    if contador<largoLista:
        numeroRandom=random.randint(contador,largoLista-1)
        lista[contador],lista[numeroRandom]=lista[numeroRandom],lista[contador]
        desordenar(lista,largoLista,contador+1)
M=[2,4,6,8,10,12,14]
desordenar(M,len(M),0)
print(M)
#=>Respuesta: Lopodemos determinar al ejecutar varias veces el algoritmo y ver que
#salen diferentes respuestas en cada una de las ejecuciones.