def siete():
   n= int(input("Numero N: "))  
   
   if n>100:
      a=101
      while a<=n:
         cubo = a*a
         print(cubo)
         a += 1
         
   else:
      print("N es menor a 100")

siete() 
