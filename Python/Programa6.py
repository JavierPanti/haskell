
def seis():
   cubo=0
   n=1
   aux=0
   a= int(input("Numero N: "))
   while n<=a:
      aux +=(n*n*n)
      n +=n
      print(aux)

seis()
