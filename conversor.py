def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cantidad de pesos " + tipo_pesos + " : ")
    pesos = float(pesos) #convierte string a float
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #cantidad de decimales, round(redondear)
    return "Tienes $" + str(dolares) + " dolares"
    # dolares = format(dolares, ".2g") #cantidad de decimales y connvierte a string
    # dolares = str(dolares) #str() convierte float a string
    # print("Tienes $" + dolares + " dolares")


def run():
    menu = """
    Bienvenido al conversor de monedas

    1 - pesos colombianos
    2 - pesos argentinos
    3 - pesos mexicanos

    Elige una opcion:
    """   # -> multilinea String con triple comillas
    opcion = input(menu)
    if opcion == '1':
        result = conversor("colombianos", 3875)    #->invoca la funcion: voy a la definicion de la funcion y ejecuto la logica
        print(result)
    elif opcion == '2':
        result = conversor("argentinos", 65)
        print(result)
    elif opcion == '3':
        result = conversor("mexicanos", 24)
        print(result)
    else:
        print("Ingrese una opcion correcta")


if __name__ == "__main__":
    run()