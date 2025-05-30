#Para escribir datos en un archivo, lo abrimos en modo de escritura ("w") utilizando la función open().
#  Si el archivo no existe, se creará automáticamente. 
# Si el archivo ya existe, su contenido se sobrescribirá.

archivo = open("datos.txt", "w") #se abre el archivo "datos.txt" en modo de escritura utilizando open().
archivo.write("Hola, mundo!") #se escribe la cadena "¡Hola, mundo!" en el archivo utilizando el método write().
archivo.close() #se cierra el archivo utilizando el método close().

#Para leer el contenido de un archivo, primero debemos abrirlo utilizando la función open() en modo de lectura ("r"). 
# Luego, podemos leer el contenido del archivo utilizando métodos como read() o readlines().

archivo = open("datos.txt", "r") #se abre el archivo "datos.txt" en modo de lectura utilizando open()
contenido = archivo.read() #e lee todo el contenido del archivo utilizando el método read() y se almacena en la variable contenido.
print(contenido) #se muestra el contenido en la pantalla
archivo.close() # se cierra el archivo utilizando el método close().

#También puedes utilizar la declaración with para manejar la apertura y cierre de archivos de manera automática.
#En este caso, el archivo se abre utilizando la declaración with y se cierra automáticamente una vez que se sale del bloque with, incluso si ocurre una excepción.

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)