nombre = input('Cuál es tu nombre?\r\n')
print(f'tu nombre es {nombre}')













#leer los datos cuando sean numeros podemos hacer un if
#NOTA LAS ENTRADAS DE DATOS SIEMPRE VIENEN EN STRING

edad = input('Cual es tu edad?')
#convertir edad en un entero
edad = int(edad)   #float #str

if edad >=18:
    print(f'eres mayor de edad y puedes votar')
else:
    print(f'lo sentimos aun eres un bebe')












nombre = input('Cuál es tu nombre?')
print(f'Tu nombre es {nombre}')


#caso que un usuario ingrese otro valor que no sea numero
edad = input('¿Cuál es tu edad?')
try:
    edad = int(edad)
    if edad >= 18:
        print(f'Eres mayor de edad y puedes votar.')
    else:
        print(f'Aún no tienes la edad para votar.')
except ValueError:
    print("Por favor, ingresa un número válido para la edad.")

