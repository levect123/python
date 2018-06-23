numeroa = float(input("Introduce el primer numero: "))
print ("El numero que ingreso es:\n",numeroa)
numerob = float(input("Introduce el segundo numero: "))
print ("El numero que ingreso es:\n",numerob)
suma = float (numeroa + numerob)
print (("el resultado en suma es:" " " + str(suma) ))

if suma < 20:
    print "azul"
elif suma < 40:
    print "rojo"
elif suma < 60:
    print "negro"
