import random


def jugar():
    usuario = input('''Escoge una opción: 
    'pi' para piedra,
    'pa' para papel y 
    'ti' parea tijera.\n''').lower()
    cpu = random.choice(['pi', 'pa', 'ti'])

    if usuario == cpu:
        return f''' Tú: {usuario} Cpu: {cpu}
                          ¡Empate!'''

    if ganó_el_jugador(usuario,cpu):
        return f'''Tú: {usuario} Cpu: {cpu}
                       ¡Ganaste!'''

    if usuario in ('pi', 'pa', 'ti'):
        return f''' Tú: {usuario} Cpu: {cpu}
                         ¡Perdiste!'''
    else:
        return 'Error, la opción que has elegido es inválida'


def ganó_el_jugador(jugador, oponente):
    # Retornar True (Verdadero) si gana el jugador.
    # Piedra gana a Tijera (pi > ti).
    # Tijera gana a Papel (ti > pa).
    # Papel gana a Piedra (pa > pi).
    if ((jugador == 'pi' and oponente == 'ti')
            or (jugador == 'ti' and oponente == 'pa')
            or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())




