#Realiza una funcion que permita obtener el maximo de 3 numeros

print "----------------------------------------------------"
print "-         Calcula el mayor de 3 de numeros         -"
print "----------------------------------------------------"
print ""

print "Escribe el primer numero: "
a = input()
print "Escribe el segundo numero: "
b = input()
print "Escribe el tercer numero:"
c = input()
print ""
print "........................................."
print "                RESULTADO                "
print ""

def mayor():
	if a > b and a > c:
		print "El mayor es: ", a

	else: 
		if b > a and b > c:
			print "El mayor es: ", b
		else:
			print "El mayor es: ", c
	return		
mayor()

print ""
print ".........................................."
print ""
print "Programa Finalizado"
print ""
	  
