dict = {}

frase = raw_input()
letras = raw_input()
letrasNaoContadas = list()
yay = 0
whoops = 0

def changeCase(letra):
	if letra == letra.upper():
		return letra.lower()
	else:
		return letra.upper()

for letra in letras:
	if letra in dict:
		dict[letra] = dict[letra] + 1
	else:
		dict[letra] = 1

for i in range(len(frase)):
	if (frase[i] in dict) and (dict[frase[i]] > 0):
		dict[frase[i]] -= 1
		yay += 1
	else:
		letrasNaoContadas.append(i)

for i in letrasNaoContadas:
	if (changeCase(frase[i]) in dict) and (dict[changeCase(frase[i])] > 0):
		dict[changeCase(frase[i])] -= 1
		whoops += 1

print "%d %d" % (yay, whoops)