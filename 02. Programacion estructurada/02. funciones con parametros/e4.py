 #EJEMPLO 2 RETORNO DE DATOS
#retorno de datos se devuelven a la llamada de la función que recoge los datos
def retorno_superficie(lado):
	sup=lado*lado
	return sup  # con la instrucción return se retorna los datos de la función
va=int(input("introduce el valor del cuadrado:"))
superficie=retorno_superficie(va) # aqui recogemos los datos que enviamos y lo almacenamos en la variable superficie
print("al algoritmo del cuadrado es:", superficie)	
