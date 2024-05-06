## Fechas ##

import datetime

print(datetime.datetime.now()) ##Con este método podemos obtener la fecha actual

fecha = datetime.datetime.now() #Tambien se puede guardar la fecha en una variable
print(fecha)

print(type(fecha)) ##Podemos ver que el tipo de dato de fecha es un tipo de dato nuevo

# Existe un método que nos permite darle un formato a las fechas para que sean más legibles, o para que estén acomodadas de una u otra forma

print(fecha.strftime("Dia de la semana abreviado: %a")) #Loq ue determina que formato se utilizará es el indicador de forma '%x' 
print(fecha.strftime("Dia de la semana completo: %A"))
print(fecha.strftime("Mes abreviado: %B "))
print(fecha.strftime("Mes abreviado: %b "))
print(fecha.strftime("Fecha completa: %c "))
print(fecha.strftime("Siglo (empieza a contar desde cero): %C "))
print(fecha.strftime("Día del mes (01 - 31): %d "))
print(fecha.strftime("Día/hora/año: %D "))
print(fecha.strftime("Día del mes (1 - 31): %e "))
print(fecha.strftime("Año en dos dígitos: %g "))
print(fecha.strftime("Año en cuatro dígitos: %G "))
print(fecha.strftime("Mes abreviado: %h "))
print(fecha.strftime("Hora (00 - 23): %H "))
print(fecha.strftime("Hora (01 - 12): %I "))
print(fecha.strftime("Día del año: %j "))
print(fecha.strftime("Mes del 01 al 12: %m "))
print(fecha.strftime("Minuto: %M "))
print(fecha.strftime("AM o PM: %p "))
print(fecha.strftime("Hora + AM o PM: %r"))
print(fecha.strftime("Hora y minutos: %R"))
print(fecha.strftime("Segundos: %S"))
print(fecha.strftime("Tabulación: %t"))
print(fecha.strftime("Hora, minutos y segundos: %T"))
print(fecha.strftime("Día de la semana (número): %u"))
print(fecha.strftime("Semana del año (empieza en domingo): %U"))
print(fecha.strftime("Semana del año(Condiciones especiales): %V"))
print(fecha.strftime("Semana del año (empieza en lunes): %W"))
print(fecha.strftime("Día de la semana (empieza en domingo): %w"))
print(fecha.strftime("Día/mes/año de dos dígitos: %x"))
print(fecha.strftime("Hora/minutos/segundos: %X"))
print(fecha.strftime("Año corto: %y"))
print(fecha.strftime("Año largo: %Y"))