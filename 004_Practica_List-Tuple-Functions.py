##Convertir lista en tupla y viceversa

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print(type(colores))
colores  = tuple(colores)
print(type(colores))

colores = list(colores)

def Prendas(**kwargs):
    for x in kwargs:
        print(kwargs[x])
x = 1
while x != 0:
    colorPrenda = input("Ingrese un color de prenda: ").lower()
    Prendas(prenda1 = "Camisa", prenda2 = "Pantalón", prenda3 = "Playera")
    if colorPrenda in colores:
        print("La prenda está diponible en: " + colorPrenda)
        answer = input("¿Desea comprarla? s/n: ")
        if answer == 's':
            print("Se ha generado la compra.")
            colores.remove(colorPrenda) ##Eliminamos el color comprado
        if answer == 'n':
            print("Adios.")
            x = 0
    else:
        answer = input("Ese color no está disponible. ¿Desea salir? s/n: ")
        if answer == 's':
            print("Adios.")
            x = 0

def SumaConsecutiva(*args):
    sumaTotal = 0
    for x in args:
        sumaTotal += x
    
    print("La suma es: ", sumaTotal)


SumaConsecutiva(1,2,3,4,5)
