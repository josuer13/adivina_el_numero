import random


def adivina_el_número(x):

    print('=========================')
    print('¡Bienvenido(a) al Juego! ')
    print('=========================')
    print('Necesitas adivinar el número que piensa la computadora.')

    número_aleatorio = random.randint(1, x) # Número aleatorio entre 1 y x.

    predicción = 0

    while predicción != número_aleatorio:
        # El usuario ingresa un número
        predicción = int(input(f'Adivina un número entre 1 y {x}: '))# f-string

        if predicción < número_aleatorio:
            print('El número no es correcto. Intenta con un número más grande.')
        elif predicción > número_aleatorio:
            print('El número no es correcto. Intenta con un número más chico.')

    print(f'¡Feliciades! has adivinado el número '
          f'{número_aleatorio} correctamente')

