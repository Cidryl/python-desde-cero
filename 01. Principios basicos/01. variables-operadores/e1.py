print ("datos de la primera persona")

# Para cargar por teclado una cadena de caracteres utilizamos la función input 
# las variables pueden tener muchas funciones aquí tenéis una la utilizamos para almacenar el valor introducido por teclado
nombre1=input("ingrese nombre del producto:")
precio1=int(input("ingrese un precio:"))
nombre2=input("ingrese nombre del producto:")
precio2=int(input("ingrese un precio:"))


# esta es una constante
BONIFICACION = 20
"""OPERADORES  ESTAS COMILLAS SON PARA PONER COMENTARIOS MAS LARGO DE UNA LINEA"""
# PARA COMENTARIOS DE UNA LINEA UTILIZAMOS ESTE SIGNO #
# sumams los dos precios y su resultado lo guardomos en una varibles
precio_compra_total = precio1 + precio2  # operador aritmético
# comprabamos si el precio1 es mayor o igual a precio2
comparar = precio1>=precio2 # operador comparación
logico = (precio1 < precio2 and precio1 == precio2) # operador lógico




cabecera="resultados del producto {0}. y del producto. {1}.:"
# contatenamos las cadenas de texto de varias formas aquí tenéis una con la función format
print (cabecera.format(nombre1, nombre2))
print ("El precio del primer valor es mayor o igual a el precio del segundo valor:") 
print(comparar) 
# concatenar se puede hacer de esta manera con el sign + y en la variable la propiedad str 
print ("la suma de los dos productos es:" + str(precio_compra_total)) 
print ("precio1 < precio2 and precio1 == precio2")
print (logico)
""" VEMOS EL OPERADOR DE ASIGNACION AQUI ABAJO """
precio_compra_total += BONIFICACION  # operador de asignación
print ("al precio total le incrementamos su valor que tiene la constante:" + str(precio_compra_total))



