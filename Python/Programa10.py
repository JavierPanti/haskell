
#10. Crear un programa que por medio de recursión calcule la suma de los cuadrados de n números.

def diez():
   n= int(input("Numero N: "))
   num=0
   
   if n>0:
      while n>=1:
         num +=n*n
         print(n,"=", num)
         n -=1
   else:
      print("Numero no valido")
     
diez()

