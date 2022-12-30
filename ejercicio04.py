#Escriba un programa recursivo y otro no recursivo para calcular n!. Compare los tiempos
#requeridos por los programas.
import time
def factorial_recursivo(n):
    if n == 1:
        return 1
    return n*factorial_recursivo(n-1)
tiempo1=time.perf_counter()
M=factorial_recursivo(8)
tiempo2=time.perf_counter()
print(M,"=> Se realizó en: ",tiempo2-tiempo1)

def factorial(n):
    b=1
    for i in range(n,1,-1):
        b*=i
    return b 
tiempo1=time.perf_counter()
N=factorial(8)
tiempo2=time.perf_counter()
print(N,"=>  Se realizó en: ",tiempo2-tiempo1)
