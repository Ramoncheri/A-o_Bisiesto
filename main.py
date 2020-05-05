import Funcion_Bisiesto

n= input("Año: ")

while not Funcion_Bisiesto.entero(n) and Funcion_Bisiesto.bisiesto(int(n)):
    print (n, "incorrecto")
    n= input ('Año: ')
    
print(n, 'es bisiesto')