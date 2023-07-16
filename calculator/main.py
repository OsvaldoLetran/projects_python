import func_maths


def run():
    option = 0
    while True:
        menu = """
        Bienvenido a la calculadora:

        1 - Suma
        2 - Resta
        3 - Multiplicacion
        4 - Division
        5 - Raiz cuadrada
        6 - Potencia a la n
        0 - Apagar calculadora

        Elige una opcion:
        """ 
        option = input(menu)

        if option == '1':
            try:
                a = int(input('Ingresa un numero: '))
                b = int(input('Ingresa un numero: '))
                print(func_maths.addition(a, b))
            except ValueError as er:
                print(er)
            
        elif option == '2':
            try:
                a = int(input('Ingresa un numero: '))
                b = int(input('Ingresa un numero: '))
                print(func_maths.subtraction(a, b))
            except ValueError as er:
                print(er)
            
        elif option == '3':
            try:
                a = int(input('Ingresa un numero: '))
                b = int(input('Ingresa un numero: '))
                print(func_maths.multiplication(a, b))
            except ValueError as er:
                print(er)
            
        elif option == '4':
            try:
                a = int(input('Ingresa un numero: '))
                b = int(input('Ingresa un numero: '))
                print(func_maths.division(a, b))
            except ValueError as er:
                print(er)

        elif option == '5':
            try:
                a = int(input('Ingresa un numero: '))
                print(func_maths.binary_search(a))
            except ValueError as er:
                print(er)

        elif option == '6':
            try:
                a = int(input('Ingresa un numero: '))
                b = float(input('Ingresa n: '))
                print(func_maths.potency(a, b))
            except ValueError as er:
                print(er)
        
        elif option == '0':
            break
            
        else:
            print("Ingrese una opcion correcta")


if __name__ == "__main__":
    run()
