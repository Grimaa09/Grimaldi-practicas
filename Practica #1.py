# Programa sencillo que cumple las condiciones que me pidió 

def es_primo(n):
    if n < 2:   
        return False
    for i in range(2, n): 
        if n % i == 0:
            return False
    return True


# contadores
pares = 0
impares = 0
primos = 0


# preguntar cuantos numeros quiere ingresar
cantidad = int(input("Cuantos numeros vas a poner: "))


for i in range(cantidad):
    num = int(input("Dame un numero: "))
    
    # par o impar
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
    
    if es_primo(num):
        primos = primos + 1


# resultados
print("Pares:", pares)
print("Impares:", impares)
print("Primos:", primos)
