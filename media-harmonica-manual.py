

"""

xh = (1/(soma(1/xj)))

xh = n/(sum(1/xj))


"""

#dados

x = [10, 60, 360];
y = [2, 2, 2, 2];

#calculo manual:

nX = len(x);

somaX = (1/x[0]) + (1/x[1]) + (1/x[2]);

print(f'Média harmônica = {nX} / {somaX:.4f}');

xH = nX / somaX;

print(f'{xH:.4f}');


#calculo sts

import numpy as np
import statistics as sts;


print(f'{sts.harmonic_mean(x)}');


#calculo com loop

#Menos chances de erro.

somaX = [(1/x[k]) for k in range (0, len(x))]

somaX = sum(somaX)

xH = nX / somaX

print(xH)

#Realizando o calculo com Y
nY = (len(y))

somaY = [(1/y[k]) for k in range (0, len(y))]
somaY = sum(somaY)

xH = nY / somaY

print(f'Média harmônica = {nY} / {somaY}');
print(xH)