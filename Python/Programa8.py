def ocho():
   print ("Realiza un programa que permita generar un intervalo de n numeros entre 20 y 60")
   n = int(input ("Dame un numero: "))
   
   if n>=20 and n<=60:
      a=n
      while a<=60:
         print(a)
         a +=1
     
   else:
      print ("Fuera del Rango 20 y 60")
ocho()
