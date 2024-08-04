
import random
numero_secreto = random.randint(0, 100)
cantidad_intentos = 0
cantidad_max_intentos = 3 
adivinado = False

print ("Bienvenido al juego de adivinaar")

while not adivinado and cantidad_intentos < cantidad_max_intentos:
    entrada = input("introduce un número del 1 al 99: ")
    numero = int(entrada)
    
    break
    
    if numero == numero_secreto:
        print("Has ganado!")
        adivinado = True
        
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
        
    else:
        print("El número es menor al ingresado")
        
    cantidad_intentos += 1
        
if not cantidad_intentos < cantidad_max_intentos: 
    print("Has perdido!")
    print("El número secreto era:", numero_secreto)

