def calcular_media (*numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma/cantidad
    return media

print ("Media: ", calcular_media(10,20,30,40))

def sumar_3(x):
    return x + 3

sumar = lambda x: x + 3

print("Sumarle 3 a un numero: ", sumar_3(5))
print("Sumarle 3 a un numero con una funcion lambda: ", sumar(10))