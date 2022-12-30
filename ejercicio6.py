#Un robot puede dar pasos de 1 o 2 metros. Escriba un programa para numerar todas las
#maneras en que el robot camina n metros.
def pasos(n):
    if n ==1 or n==2:
        return n
    else:
        return pasos(n-1)+pasos(n-2)
print(pasos(5))