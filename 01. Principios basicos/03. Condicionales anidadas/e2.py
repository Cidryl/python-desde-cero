nota1=int(input("Ingrese primer nota:"))
nota2=int(input("Ingrese segunda nota:"))
nota3=int(input("Ingrese tercer nota:"))
media=(nota1+nota2+nota3)/3

if media == 9 or media == 10:
	print ("sobresaliente")
elif media == 5:
	print ("suficiente")
elif media == 6:
    print ("bien")
elif media == 7 or media == 8:
    print ("regular/bien") 
else:
    print ("insuficiente")       	
	             

	            