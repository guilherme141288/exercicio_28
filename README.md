# exercicio_28

#finding even or odd numbers

inp = int( input ('\033[4;35;40mMe diga um numero qualquer:    \033[m'))

new = inp % 2
if new == 0:
    print ('o numero {} é um numero par' .format(inp))
else:
    print ('o numero {} é um numero impar' .format (inp))
