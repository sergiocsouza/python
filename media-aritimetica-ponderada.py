

"""
Média aritimética ponderada

soma(dados*pesos)/soma(pesos)

"""

pesos = [1, 2, 3, 4];
notas = [8, 7, 9, 9];

notasXpesos = [notas[i] * pesos[i] for i in range(0, len(notas))];
media_pond = sum(notasXpesos) / sum(pesos);

media_pond


print(media_pond);