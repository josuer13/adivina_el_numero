import adivina_el_numero
import adivina_el_numero_cpu

print('¡Hola!')
print('Si quieres adivinar el número que piensa la cpu,')
print('escribe: 1.')
print('Si quieres que la cpu adivine el número que tu piensas,')
print('escribe: 2.')
respuesta = int(input('Escribe que vas a jugar: '))
if respuesta == 1:
    adivina_el_numero.adivina_el_número(10)
else:
    adivina_el_numero_cpu.adivina_el_número_cpu(10)
