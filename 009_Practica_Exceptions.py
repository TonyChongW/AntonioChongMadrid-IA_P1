
print("a/b")
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")

try:                                                    ## Dentro del try se realiza la acción que podría generar un error
   
    x = a/b                                             ## La acción que puede generar un error es la división, ya que no se puede dividir sobre cero
   
    print(x)                                            ## Si no hay error, se imprime el resultado de la división

except:                                                 ## En caso de que se divida sobre cero, se manda a llamar la excepciópn que ejecuta una acción para evitar el error
    
    print("Error, no se puede dividir entre 0")         ## En este caso se motrará un mensaje
