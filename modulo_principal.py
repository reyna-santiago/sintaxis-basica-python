import modulo_operaciones
import modulo_utilidades


resultado = modulo_operaciones.sumar(5, 3)
modulo_utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = modulo_utilidades.obtener_nombre_usuario()
modulo_utilidades.imprimir_mensaje(f"Hola, {nombre}!")