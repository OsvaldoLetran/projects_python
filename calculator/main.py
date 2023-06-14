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
            a = int(input('Ingresa un numero: '))
            b = int(input('Ingresa un numero: '))
            print(func_maths.addition(a, b))
            
        elif option == '2':
            a = int(input('Ingresa un numero: '))
            b = int(input('Ingresa un numero: '))
            print(func_maths.subtraction(a, b))
            
        elif option == '3':
            a = int(input('Ingresa un numero: '))
            b = int(input('Ingresa un numero: '))
            print(func_maths.multiplication(a, b))
            
        elif option == '4':
            a = int(input('Ingresa un numero: '))
            b = int(input('Ingresa un numero: '))
            print(func_maths.division(a, b))

        elif option == '5':
            a = int(input('Ingresa un numero: '))
            print(func_maths.binary_search(a))

        elif option == '6':
            a = int(input('Ingresa un numero: '))
            b = float(input('Ingresa n: '))
            print(func_maths.potency(a, b))
        
        elif option == '0':
            break
            
        else:
            print("Ingrese una opcion correcta")


if __name__ == "__main__":
    run()
