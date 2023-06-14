import random


def run():
    numero_aleatorio = random.randint(1, 10)   #->randit para escoger numeros random integer
    numero_elegido = int(input("Elige un numero del 1 al 10: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un numero más grande")
        else:
            print("Busca un numero más pequeño")
        numero_elegido = int(input("Elige otro número: "))    #->a la altura de if
    print("¡Ganaste!")


if __name__ == "__main__":
    run()