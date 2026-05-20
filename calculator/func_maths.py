def decorador(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return f"Error en {func.__name__}: {str(e)}"
        return wrapper

class Calculator:

    @decorador
    def addition(self, a: int | float, b: int | float) -> int | float:
        return a + b

    @decorador
    def subtraction(self, a: int | float, b: int | float) -> int | float:
        return a - b

    @decorador
    def multiplication(self, a: int | float, b: int | float) -> int | float:
        return a * b

    @decorador
    def division(self, a: int | float, b: int | float) -> int | float:
        return a / b if b != 0 else "Error: You cannot divide by zero"

    @decorador
    def sqrt(self, a: int | float) -> int | float:
    #binary search
        if a < 0:
            return "Error: No se puede calcular raíz de número negativo"
        if a == 0:
            return 0.0

        epsilon = 1e-6    #es mas preciso, también epsilon = 0.001
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
        return result

    @decorador
    def potency(self, a: int | float, b: int | float) -> int | float:
        return a**b