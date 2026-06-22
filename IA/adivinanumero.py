import random
 
def obtener_numero_personalizado():
    rango_inferior = int(input("Ingresa el rango inferior de números: "))
    rango_superior = int(input("Ingresa el rango superior de números: "))
    return rango_inferior, rango_superior
 
 
def obtener_numero_ingresado(rango_inferior, rango_superior):
    while True:
        try:
            numero_ingresado = int(
                input(f"Ingresa un número entre {rango_inferior} y {rango_superior}: "))
            if rango_inferior <= numero_ingresado <= rango_superior:
                return numero_ingresado
            else:
                print("El número ingresado está fuera del rango especificado.")
        except ValueError:
            print("Error: Ingresa un número válido.")
 
 
def obtener_puntuacion(intentos, ganado=True):
    if not ganado:
        return 'No acertaste dentro de los 10 intentos. Intenta de nuevo.'
    if intentos <= 5:
        return 'Excelente ⭐⭐⭐⭐⭐'
    elif intentos <= 10:
        return 'Bueno ⭐⭐⭐⭐'
    elif intentos <= 15:
        return 'Regular ⭐⭐⭐'
    else:
        return 'Intenta mejorar 👍'

def mostrar_mejores_puntajes():
    print("---- Mejores Puntajes ----")
    try:
        with open("mejores_puntajes.txt", "r") as archivo:
            puntajes = archivo.readlines()
            if not puntajes:
                print("No hay puntajes registrados.")
            else:
                for puntaje in puntajes:
                    print('👉', puntaje.strip(), "intentos")
    except FileNotFoundError:
        print("No hay puntajes registrados.")
    print("--------------------------")
 
 
def actualizar_mejores_puntajes(intentos):
    try:
        with open("mejores_puntajes.txt", "a") as archivo:
            archivo.write(f"{intentos}\n")
        print("Los mejores puntajes se han actualizado.")
    except IOError:
        print("Error al guardar los puntajes.")
 
 
# Configuración inicial
print("Bienvenido al juego de adivinar el número.")
opcion = input("¿Deseas utilizar un rango de números personalizado? (s/n): ")
 
if opcion.lower() == "s":
    rango_inferior, rango_superior = obtener_numero_personalizado()
else:
    rango_inferior, rango_superior = 1, 100
 
numero_objetivo = random.randint(rango_inferior, rango_superior)
 
# Bucle principal del juego
max_intentos = 10
intentos = 0
ganado = False
while True:
    numero_ingresado = obtener_numero_ingresado(rango_inferior, rango_superior)
    intentos += 1
 
    if numero_ingresado < numero_objetivo:
        print("El número ingresado es demasiado bajo.")
    elif numero_ingresado > numero_objetivo:
        print("El número ingresado es demasiado alto.")
    else:
        print('🎉 ¡Felicidades! Adivinaste el número correcto.')
        ganado = True
        break
 
    diferencia = abs(numero_objetivo - numero_ingresado)
    if diferencia <= 10:
        print("Estás muy cerca del número correcto.")
    elif diferencia <= 20:
        print("Estás cerca del número correcto.")
    else:
        print("Estás lejos del número correcto.")
 
    if intentos >= max_intentos:
        print(f"Lo siento, no adivinaste el número en {max_intentos} intentos.")
        print(f"El número correcto era {numero_objetivo}.")
        break
 
# Mostrar puntuación y mejores puntajes
puntuacion = obtener_puntuacion(intentos, ganado)
if ganado:
    print('¡Has completado el juego! 🥳')
    print("Número de intentos:", intentos)
    print("Tu puntuación:", puntuacion)
else:
    print('Juego terminado. Mejor suerte la próxima.')
    print("Número de intentos:", intentos)
    print("Tu puntuación:", puntuacion)
 
# Actualizar mejores puntajes
if ganado:
    actualizar_mejores_puntajes(intentos)
 
# Mostrar mejores puntuaciones
mostrar_mejores_puntajes()