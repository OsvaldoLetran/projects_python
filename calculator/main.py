import func_maths

def get_number(prompt = "Ingresa un número: "):
    try:
        return float(input(prompt))
    except ValueError:
        print("Error: Ingresa un número válido")

MENU = """
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

def run():
    calc = func_maths.Calculator()

    operations = {
        '1': calc.addition,
        '2': calc.subtraction,
        '3': calc.multiplication,
        '4': calc.division,
        '6': calc.potency,
    }

    while True: 
        option = input(MENU).strip()

        if option in operations:
            operacion = operations[option]
            a = get_number('Primer número: ')
            b = get_number('Segundo número: ')
            print(f"Resultado: {operacion(a, b)}\n")

        elif option == '5':
            a = get_number('Número: ')
            print(f"Resultado: {calc.sqrt(a)}\n")

        elif option == '0':
            print("Apagando calculadora...")
            break

        else:
            print("Opción no válida\n")

if __name__ == "__main__":
    run()