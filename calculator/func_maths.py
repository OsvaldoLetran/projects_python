def decorador(func):
    def wrapper(*args):
        _resultado = func(*args)
        return _resultado
    return wrapper


@decorador
def addition(a: int, b: int):
    try:
        result = a + b
    except TypeError as er:
        result = er
    
    return result


@decorador
def subtraction(a: int, b: int):
    try:
        result = a - b
    except TypeError as er:
        result = er
    
    return result


@decorador
def multiplication(a: int, b: int):
    try:
        result = a*b
    except TypeError as er:
        result = er
    
    return result


@decorador
def division(a: float, b: float):
    try:
        result = a / b
    except ZeroDivisionError as e:
        result = e
    except TypeError as er:
        result = er
    
    return result


@decorador
def binary_search(a: float):
    try:
        epsilon = 0.001
        lower = 0.0
        higher = max(1.0, a)
        result = (higher + lower) / 2

        while abs(result**2 - a) >= epsilon:
            # print(f'bajo= {lower}, alto= {higher}, respuesta= {result}')
            if result**2 < a:
                lower = result
            else:
                higher = result

            result = (higher + lower) / 2
    except TypeError as er:
        result = er

    return result


@decorador
def potency(a: float, b: float):
    try:
        result = a**b
    except TypeError as er:
        result = er
    
    return result
