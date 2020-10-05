#EJEMPLO2
#RETORNO DE LISTA
def cargar_lista():
	li=[]
	for x in range(5):
		valor=int(input("introduce valor:"))
		li.append(valor)
	return li
def imprimir_mayor(li):
	print("valores de la lista mayores a 10:")
	for x  in range(len(li)):
		if li[x]>10:
			print(li[x])
lista=cargar_lista()
imprimir_mayor(lista)			
