#EJEMPLO2
# PARAMETRO ARBITRARIOS
def sumar(v1, v2, *lista):
	suma=v1+v2
	for x in range(len(lista)):
		suma=suma+lista[x]
	return suma	
print("Suma de dos valores")
print(sumar(1,2))
print("suma de cuatro valores")
print(sumar(1,2,3,4))
print("suma de diez valores")
print(sumar(1,2,3,4,5,6,7,8,9,10))

