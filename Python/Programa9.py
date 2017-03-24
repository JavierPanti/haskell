#   9. Realiza un programa que solicite dos argumentos de tipo Double para calcular la hipotenusa de un triángulo rectángulo y #retorne un valor de tipo Double.
import math

def nueve():
   
      num1=float (input("Ingrese numero x: "))
      num2=float (input("Ingrese numero y: "))
   
      suma= (num1**2) + (num2**2)
      h=float(math.sqrt(suma))
      print("")
      print ("La hipotenusa es: ", h)
         
   
nueve()

