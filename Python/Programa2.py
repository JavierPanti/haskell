#Volumen esfera python

import math 

print "----------------------------------------"
print "-   CALCULA EL VOLUMEN DE UNA ESFERA   -"
print "----------------------------------------"
print ""
print ""
print "Escribe el valor del radio: "
r = float(input())

p = (float(3.1416))
frac = (float(0.75))


print "El radio de la esfera es de: ", r, "cm"

print ""
def volumenesfera():
	resultado = ((p*frac)*(r**3))
	print "...................................................."
	print "                    RESULTADO                      "
	print "                                                  "
	print "El radio de la esfera es de: ", r, "cm            "
	print "                                                  "
	print "El volumen de la esfera es:                       "
	print "",resultado,"                                     "
	print "....................................................."
	return

volumenesfera()
print ""
print ""
print "Programa Finalizado"
print ""
