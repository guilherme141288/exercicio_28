#guessing game using random lib

from random import randint



print ('vou pensar em um numero de 0 a 5. Tente adivinhar...')
ran = randint(0 , 5)

entrada = int (input ('em que numero pensei? '))


if ran == entrada:
    print ('Parabens voce conseguiu!!')
else:
    print ('ganhei eu pensei no numero {}' .format(ran))