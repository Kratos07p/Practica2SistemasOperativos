continuar = True
totalVenta = 0
cantidadVenta = 0

def inputNumber(mensaje, isFloat = False):
    while True:
        try:
            if isFloat:
                return float(input(mensaje))
            return int(input(mensaje))
        except ValueError:
            print("Opps!!! el dato ingresado no es una entrada valida, ingrese de nuevo")

while continuar == True:
    cantidad = inputNumber("Ingrese el cuanta cantidad del producto se ha comprado: ")
    precio = inputNumber("Ingrese el precio del producto: ", True)

    totalSinDescuento = cantidad * precio

    if cantidad >= 5 and cantidad <=10:
        totalVenta += totalSinDescuento - (totalSinDescuento * 0.05)

    elif cantidad >= 11 and cantidad <=20:
        totalVenta += totalSinDescuento - (totalSinDescuento * 0.10)
    
    elif cantidad > 20:
        totalVenta += totalSinDescuento - (totalSinDescuento * 0.15)

    else:
        totalVenta += (totalSinDescuento)
    
    cantidadVenta += cantidad

    opcion = input("Continuar? S/N: ")

    if opcion.upper() == 'N':
        continuar = False

print(f"Total de productos: {cantidadVenta}")
print(f"Total a pagar: ${totalVenta}")
print("Gracias por Comprar")