def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue     #interrumpe el ciclo for para seguir iterando el sig. if y el if fuera del bloque for
        if numero % i == 0:
            contador += 1
    if contador == 0 and numero != 1:
        return True
    else:
        return False


def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):    #->esto sin declararlo es igual a True
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()
