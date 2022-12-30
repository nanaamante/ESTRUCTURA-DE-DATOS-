#Escriba un programa recursivo y otro no recursivo para calcular la sucesión deFibonacci.
#Compare los tiempos requeridos por los programas
import time
def fibonacci_recursivo(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)
tiempo1=time.perf_counter()
fibonacci_recursivo(10)
tiempo2=time.perf_counter()
print("El Fibonacci recursivo demoró: ",tiempo2-tiempo1)

def fibonacci(m):
    a=0
    b=1
    for k in range(m+1):
        c=b+a
        a=b
        b=c
    return a
tiempo1=time.perf_counter()
fibonacci(10)
tiempo2=time.perf_counter()
print("El Fibonacci no recursivo demoró: ",tiempo2-tiempo1)