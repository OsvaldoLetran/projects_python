import random


def generar_contrasena():
    mayus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    simbols = ["!", "#", "$", "%", "&", "/", "(", ")", "¿", "?"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = mayus + minus + simbols + numbers

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)    #-> con la funcion choice eligo un caracter al azar de lista caracteres
        contrasena.append(caracter_random)

    contrasena = ''.join(contrasena)    #-> con esta linea genero un string de la lista original
    return contrasena


def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == "__main__":
    run()