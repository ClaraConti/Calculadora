


print("hola Profesor")
print("Hola soy su alumna")

menu=""" Bienvenido a nuestra calculadora, 
seleccione un nùmero de 1 al 4: 

[1] Sumar
[2] Restar
[3] Multiplicar
[4] Dividir

"""

print (menu)

opcion= input ("ingrese un numero: ")
if opcion == '1' :
    def suma (x,y):
        try :
            s=x+y 
        except TypeError :
            print ("lo siento ,solo son permitidos numeros numericos ")
elif opcion == '2' :
    pass
elif opcion == '3':
    pass
elif opcion == '4':
    pass
    
else :
    print ("Debes de digitar un numero entre el 1 y 4")









 


