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


    # ESTE ES EL SEGUNDO EJEMPLO CON LA INSTRUCCION IF/ELSE

sueldo1=int(input("introduce el sueldo1:"))
sueldo2=int(input("introduce el sueldo2:"))

# codicional if / esle
if sueldo1>sueldo2:
	print ("el sueldo1/ :" + str(sueldo1) + " es mayor que sueldo2/ " + str(sueldo2))
else:
	print ("el sueldo1/ :" + str(sueldo1) + " es menor que sueldo2/ " + str(sueldo2))


	
