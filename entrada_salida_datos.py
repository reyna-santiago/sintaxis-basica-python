#se solicita al usuario que ingrese su nombre y edad utilizando la función input(). 
#Los valores ingresados se almacenan en las variables nombre y edad, respectivamente. Luego, se utilizan estas variables para mostrar un saludo personalizado en la pantalla.

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

#En este ejemplo, se solicita al usuario que ingrese su edad y se convierte el valor ingresado a un número entero utilizando int(). 
# Luego, se utiliza una estructura condicional para verificar si la edad es mayor o igual a 18 y mostrar un mensaje correspondiente.

edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#Podemos utilizar la f-string (formateo de cadenas) para incrustar variables directamente dentro de una cadena de texto.
#En este caso, las variables se incrustan dentro de la cadena utilizando llaves {} y se precede la cadena con la letra f para indicar que es una f-string
nombre = "Juan"
edad = 25


print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")