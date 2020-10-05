def retornar(d1, d2):
	if d1 > d2:
		m=d1
	else:
		m=d2
	return m
	
d1=34
d2=56
print(retornar(d1,d2)) # se puede utilizar la llada a la función para obtenr el valor retornado
valor=retornar(d1, d2) # o se puede almacenar el valor en una variable y luego operar con el	
print ("el valor mayor es:", valor)	
	   	