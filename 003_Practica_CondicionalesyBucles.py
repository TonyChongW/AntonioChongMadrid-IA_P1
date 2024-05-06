x = 1
while x != 0:
    x = int(input("Seleccione una operacion: \n1.- Suma\n2.-Resta\n3.-Multiplicación\n4.-Divisón\n"))
    if x == 1:
        a = int(input("Ingrese el primer operando: "))
        b = int(input("Ingrese el segundo operando: "))
        suma = a + b
        print("La suma es: ", suma)
    
    elif x == 2:
        a = int(input("Ingrese el primer operando: "))
        b = int(input("Ingrese el segundo operando: "))
        resta = a - b
        print("La suma es: ", resta)
    elif x == 3:
        a = int(input("Ingrese el primer operando: "))
        b = int(input("Ingrese el segundo operando: "))
        producto = a * b
        print("El producto es: ", producto)
    elif x == 4:
        a = int(input("Ingrese el primer operando: "))
        b = int(input("Ingrese el segundo operando: "))
        if b == 0:
            print("Error, no se puede dividir sobre 0.")
        else:
            división = a / b
            print("La división es: ", división)
    elif x == 0:
        print("Adiós...")
    else:
        print("Ingrese un valor válido.")
