from abc import ABC , abstractmethod
import math
#clase abstracta figura ya que las figuras implementaran los metodos 
class Figura(ABC):
    @abstractmethod
    def __init__(self,tipofigura):
        pass
    @abstractmethod
    def area():
        pass
    @abstractmethod
    def perimetro():
        pass

    def __repr__(self):
        return f'{self.tipofigura}'
       
    
#clase cuadrado
class cuadrado(Figura):
   def __init__(self,lados,tipofigura):
       super().__init__(tipofigura)
       self.lados = lados
       self.tipofigura = tipofigura
    
   def area(self):
       area = self.lados **2
       return area
   
   def perimetro(self):
       perimetro = 4 * (self.lados)
       return perimetro
   
#clase ccirculo
class circulo(Figura):
     def __init__(self,radio,tipofigura):
        super().__init__(tipofigura)
        self.radio = radio
        self.tipofigura = tipofigura

     def area(self):
         area = math.pi  * (self.radio **2)
         return area
       
   
     def perimetro(self):
         perimetro = 2 * math.pi * self.radio
         return perimetro

#clase rectangulo
class rectangulo(Figura):
    def __init__(self,longitud,ancho,tipofigura):
       super().__init__(tipofigura)
       self.longitud = longitud
       self.ancho = ancho
       self.tipofigura = tipofigura

    def area(self):
        area = self.longitud * self.ancho
        return area
   
    def perimetro(self):
         perimetro = 2 * (self.longitud + self.ancho)
         return perimetro