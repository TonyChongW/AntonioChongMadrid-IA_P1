        ## Expresiones Regulares ## 

import re 


texto ="Esta es una prueba para ver como funciona al función search"

busqueda = re.search("i", texto) 
print(busqueda)                 ## Aqui nos imprime la primera coincidencia que tuvo con el valor a buscar y su posición

busqueda = re.search("search", texto)
print(busqueda)                 ## Aqui buscamos una palabra entera, por lo que la posición en span es más grande

busqueda = re.search("Pedro", texto)
print(busqueda)                 ## Aquí no hay coincidencias, por lo que regresa "none"


texto = "Pepe quiere un tren verde"


busqueda = re.findall("e", texto)
print(busqueda)                 ## Aquí nos imprime una lista con todas las coincidencias de dicha busqueda, como hay 7 'e' en el texto nos imprime 7 'e'

busqueda = re.findall("o", texto)
print(busqueda)                 ## Aquí nos imprime una lista vacía ya que no hay coincidencia

print(type(busqueda)) ## Podemos ver que efectivamente, findall nos retorna una lista

## Split() ## 

x = re.split(" ", texto) ## Split nos divide una cadena de texto en base a un parámetro que le pongamos, en este caso cuando encuentre un espacio tomará lo anterior como un valor singular
print(x)

texto = "Pepe/quiere/un/tren/verde"
x = re.split("/", texto)    ## En este otro caso toma '/' como el parámetro para dividir
print(x)

x = re.split("/",texto,3) ## Si le agregamos un numero como tercer parametro, este numero indicara la cantidad máxima de elemento que queremosw
print(x)

## Sub() ## 

x = re.sub("/"," ",texto) ## Sub() reemplaza un valor especificado por otro en el string, en este caso, se reemplazo la '/' por un espacio en blanco
print(x)

x = re.sub("/"," ",texto,3) ## Al igual que con split, tambien se puede limitar el numero de valores reemplazados con un parametro más
print(x) 