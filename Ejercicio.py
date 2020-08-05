
from random import randrange
import time
from os import system




if __name__ == '__main__':
    print("Iniciando...")
    lista = []
    # Genera 5 números aleatorios
    for i in range(5):
        lista.append(randrange(10))

    # Muestra lista de números generados
    print("Números generados: ")
    print(lista)

    # Espera un tiempo prudente
    time.sleep(2)  # espera en segundos

    # Limpia pantalla, solo válido en CMD
    system("cls")

    # Adivine los números
    print("Adivine los números")

    lista_verificacion = []
    for j in range(5):
        lista_verificacion.append(int(input("Introduce el " + str(j) + " valor: ")))
        pass

    print("Usted ingresó: ")
    print(lista_verificacion)

    # Verifica igualdad

    for i in range(5):
        print("Verificando el " + str(i) + " valor ")
        # print("Original: "+str(lista[i]))
        # print("Usuario: "+str(lista_verificacion[i]))
        if lista[i] == lista_verificacion[i]:
            print(str(i) + "> Acertó")
        else:
            print(str(i) + "> No acertó")

    # Evita que se cierre la ventana
    time.sleep(20)
