## Practica 2 ##
##Esta practica abarca del capitulo 7 hasta el capitulo 9 ##
import math

class Calculadora:
   operandos = []
   a = 0
   b = 0
   
   def __init__(self):
      return
   
   def Suma(self):
      sumaTotaL = 0
      x = 1
      while(x != 0):
         x = input("Ingrese un numero a sumar o 0 para salir: ")
         x = int(x)
         if x != 0:
            self.operandos.append(x)
      #for number in range operandos:
      #  sumaTotal += number
      if len(self.operandos) == 0:
         sumaTotal = 0
      else:
         sumaTotal = sum(self.operandos)
      print("La suma es: ", sumaTotal)
      self.operandos.clear()


   def SumaTwoOperands(self):
      print("a + b")
      self.a = int(input("Ingrese el valor de 'a': "))
      self.b = int(input("Ingrese el valor de 'b': "))
      suma = self.a + self.b
      print("La suma es: ", suma)
      self.a = 0
      self.b = 0
   

   def Resta(self):
      print("a - b")
      self.a = int(input("Ingrese el valor de 'a': "))
      self.b = int(input("Ingrese el valor de 'b': "))
      resta = self.a - self.b
      print("La resta es: ", resta)
      self.a = 0
      self.b = 0
      
   def Division(self):
      print("a/b")
      self.operandos.insert(0,float(input("Ingrese el valor de a: ")))
      self.operandos.insert(1,float(input("Ingrese el valor de b: ")))
      if self.operandos[1] == 0:
         print("Error")
         self.operandos.remove(0)
      else:
         print(self.operandos[0] / self.operandos[1])
   

class Circle:
   radius = 0
   perimeter = 0
   area = 0

   def __init__(self):
      return 

   def setRadius(self):
      self.radius = float(input("Ingrese el valor del radio del circulo: "))
   
   def Perimeter(self):
      self.perimeter = round((math.pi)*(2*self.radius)) 
   
   def Area(self):
      self.area = (math.pi)*(math.pow(self.radius,2)) ##radius ** 2
   
   def showDataCircle(self):
      print("Radio: ", self.radius)
      print("Perimetro: ", self.perimeter)
      print("Area: ",self.area)

c = Calculadora()
c.SumaTwoOperands()
c.Resta()
c.Division()

x = Circle()

x.setRadius()
x.Perimeter()
x.Area()
x.showDataCircle()

