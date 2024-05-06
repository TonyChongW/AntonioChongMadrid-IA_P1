## Funciones lambda e importar módulos ##

import math

class Circle:
   radius = 0
   perimeter = 0
   area = 0

   def __init__(self,radius):
      self.radius = radius 

   def setRadius(self):
      self.radius = float(input("Ingrese el valor del radio del circulo: "))
   
   def getRadius(self):
        return self.radius
   
   def Perimeter(self):
      self.perimeter = round((math.pi)*(2*self.radius)) 
   
   def Area(self):
      self.area = (math.pi)*(math.pow(self.radius,2)) ##radius ** 2
   
   def showDataCircle(self):
      print("Radio: ", self.radius)
      print("Perimetro: ", self.perimeter)
      print("Area: ",self.area)


area = lambda radio: (pow(radio,2)*math.pi)
c1 = Circle(4)
print(area(c1.getRadius()))




