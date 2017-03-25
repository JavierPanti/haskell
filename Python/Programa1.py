#Calcular media de 3 numeros
print "------------------------------------"
print "-    CALCULA MEDIA DE 3 NUMEROS    -"
print "------------------------------------"
print ""
print ""
print "Escriba el primer numero: "
a = input()

print "Escriba el segundo numero: " 
b = input()

print "Escriba el tercer numero: "
c = input()


#Calcular la media
def escribe_media():
	media = (a + b + c)/3
	print ""
	print "........................................................."
	print "                         RESULTADO                       "
	print ""
	print "la media de: ", a, ",", b, "y", c, "es:",  media
	print ""
	print "........................................................."
	return

escribe_media()
print ""
print "Programa Finalizado"
print ""