# utilizamos función input para introducir valores por teclado
sueldo=int(input("introduce el sueldo:"))
# codicional if 
if sueldo>3000:
	print("el usuario debe pagar un porcentage en impuestos")
if sueldo<=3000:  #operador de comparación
    print("El usuario esta exento de declarar su renta")

if sueldo>6000 and sueldo<10000: # operador lógico se tiene que cumplir las dos condiciones
    print("El usuario tiene que pagar una bonificación de 1000 euros")

if sueldo==20000 or sueldo==30000: #operador lógico sólo se tiene que cumplir una de las dos condiciones
    print("El usuario paga un 10 por ciento de su sueldo")	
