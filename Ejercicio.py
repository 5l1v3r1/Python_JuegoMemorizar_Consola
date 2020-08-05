from random import randrange
import time
from os import system

# Retorna Falso si hubo un error, o True si todo fue correcto
def Verifica(lista1, lista2):
    # Verifica igualdad
    gano = True    # Bool [Gano o perdió]
    for i in range(5):
        print("Verificando el " + str(i) + " valor ")
        # print("Original: "+str(lista[i]))
        # print("Usuario: "+str(lista_verificacion[i]))
        if lista1[i] == lista2[i]:
            print(str(i) + "> Acertó")
        else:
            gano = False
            print(str(i) + "> No acertó")
    return gano

# Retorna un segundo si subio de nivel, y 0 si no subió de nivel
def Nivel(lista1, lista2):
    if Verifica(lista1,lista2):
        return 1
    else:
        return 0

# Limpia pantalla
def LimpiarPantalla():
    print("\n\n\n\n")
    system("cls")

# Espera..
def Delay(n):
    for i in range(n):
        time.sleep(1)  # espera en segundos
        print("Esperando: " +str(i+1)+ " segundos")


if __name__ == '__main__':
    delay = 5   # Tiempo de nivel
    lista = []  # Lista Vacía
    lista_verificacion = [] # Lista que Usuario Rellenará
    nivel = 1
    for x in range(5) :
        def juego(lista,delay, nivel):
            LimpiarPantalla()
            print("Juego Adivina Nivel: " + str(nivel))
            lista = []
            lista_verificacion = []
            # Genera 5 números aleatorios
            for i in range(5):
                lista.append(randrange(10))
            # Muestra lista de números generados
            print("Números generados: ")
            print(lista)

            # Espera un tiempo prudente
            Delay(delay)
            LimpiarPantalla()  # Limpia pantalla, solo válido en CMD
            # Adivine los números
            print("Usted debe adivinar los números")
            for j in range(5):
                def ingresa():
                    try:
                        lista_verificacion.append(int(input("Introduce el " + str(j + 1) + " valor: ")))
                    except:
                        print("Error al ingrear el dato, vuelve a ingresarlo")
                        ingresa()

                ingresa()

            print("Usted ingresó los siguientes números: ")
            print(lista_verificacion)
            if Verifica(lista,lista_verificacion):
                return True
            else:
                return False


        if juego(lista,delay, nivel):
            nivel = nivel +1    # Subió de nivel
            delay = delay -1
            print("Felicitaciones , usted subió de nivel")
            LimpiarPantalla()
        else:
            print("Error, usted no pudo subir")
            LimpiarPantalla()
            juego(lista,delay, nivel)

    # Evita que se cierre la ventana
    time.sleep(20)