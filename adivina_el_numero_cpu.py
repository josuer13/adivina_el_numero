import random


def adivina_el_número_cpu(x):

    print('=========================')
    print('¡Bienvenido(a) al Juego! ')
    print('=========================')
    print(f'Selecciona un número entre 1 y {x} para que la '
          f'cpu intente adivinarlo...')
    límite_inferior = 1
    límite_superior = x

    respuesta = ''
    while respuesta != 'c':
        # Generar predicción
         if límite_inferior != límite_superior:
             predicción = random.randint(límite_inferior, límite_superior)
         else:
             predicción = límite_inferior # también se puede poner el:
             # límite_superior.

         # Obtener respuesta del usuario
         respuesta = input(f'''mi predicción es {predicción}. 
Si la respuesta es menor, ingresa (-).
Si la respuesta es mayor (+)
Si la respuesta es correcta, ingresa (=)''')\
             .lower()

         if respuesta == 'a':
             límite_superior = predicción - 1
         elif respuesta == 'b':
             límite_inferior = predicción + 1

    print(f'¡La cpu adivino el número: {predicción} correctamente!')


