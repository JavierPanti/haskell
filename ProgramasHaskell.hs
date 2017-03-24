-- Haskell By: Javier Panti 
-- Programa #1 Promedio de 3 numeros

medNum x y z = (x+y+z)/3

-- Programa #2 Volumen de una esfera

volumEsf v = (4/3)*pi*v^3

-- Programa #3 Numeros impares empezando desde el numero 13

imprimeTrece = [13,15..29]

-- Programa #4 Determinar el numero mayor entre 3 numeros

maxNum x y z = max x (max y z)

-- Programa #5 Rotar una lista de numeros

rota pos list = drop pos list ++ take pos list

-- Programa #6 Suma de n numeros elevados a cubo

numcubos = [x*3 | x <- [1..10]]
sumaNumcubos = sum[x*3 | x <- [1..10]]

--Programa #7 cuadrados de n numeros mayores a 100

numMayCien = [x*x | x <- [11..2]]

--Programa #8 intervalo de N numeros de 20 a 60

nNum = [20,21..60]

-- Programa #9 calcular hipotenusa con variable double

hipotenusa ::Double-> Double-> Double
hipotenusa a b = sqrt (a^2 + b^2)

-- Programa #10 por medio de recursion calcule la suma de los cuadrados de n numeros 
nume n= sum [ (x^2) | x <- reverse[1..n], x<=n ]