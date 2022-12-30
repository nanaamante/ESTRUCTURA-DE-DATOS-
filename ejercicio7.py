#Un robot puede dar pasos de 1, 2 o 3 metros. Escriba un programa para numerar todas las
#maneras en que el robot camina n metros.
def pasos(n):
    if n==1 or n==2 or n==3:
        return n
    return pasos(n-1)+pasos(n-2)+pasos(n-3)
print(pasos(10))