# Este es un juego de adivinar el número.
import random
numeroSecreto = random.randint(1, 20)
print('Estoy pensando en un número entre 1 y 20.')

# Pedir al jugador que adivine 6 veces.
for intentosRealizados in range(1, 7):
    print('Haz una suposición.')
    intento = int(input())

    if intento < numeroSecreto:
        print('Tu suposición es demasiado baja.')
    elif intento > numeroSecreto:
        print('Tu suposición es demasiado alta.')
    else:
        break   # ¡Esta condición es la suposición correcta!

if intento == numeroSecreto:
    print('¡Buen trabajo! Adivinaste mi número en ' + str(intentosRealizados) + ' intentos.')
else:
    print('No. El número en el que estaba pensando era ' + str(numeroSecreto))
