def suma(t, c):
        try :
            m= t+c
        
        except TypeError:
            print ("Lo siento, solo son permitidos valores numericos")
        else:
            return m
def divide(x, y ):
        try :
            z= x/y
        except ZeroDivisionError:
            print ("Lo siento està dividiendo entre cer")
        except TypeError:
            print ("Lo siento, solo son permitidos valores numericos")
        else:
            return z
        finally: 
             print("Fin")


print("hola  mundo soy clara")
print("Hola soy")

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
    t=float (input ("ingrese numero 1: "))
    c=float(input("Ingrese numero 2: ")) 
    result = suma(t,c)
    print (result)
elif opcion == '2' :
    pass
elif opcion == '3':
    pass
elif opcion == '4':
    x=float (input ("ingrese numero 1.: "))
    y=float(input("Ingrese numero 2: ")) 
    result = divide(x,y)
    print (result)
    
    
else :
    print ("Debes de digitar un numero entre el 1 y 4")









 


