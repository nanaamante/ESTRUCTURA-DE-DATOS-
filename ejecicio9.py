#Implemente un programa recursivo que sume dos números a + b. Considera que la suma
#a+b = a + 1 + 1 + ...+ 1 (b veces)
def suma(a,b):
    if b == 0:
        return a
    elif a ==0:
        return b
    else:
        return 1 + suma(a,b-1)
print(suma(8,10))