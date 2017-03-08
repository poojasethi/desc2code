# replacement
# codeforces 570-C

tPalavra, q = map(int, raw_input().split())
palavra = [c for c in raw_input()]

def countdots():
	pontos = 0
	
	for i in xrange(len(palavra) - 1):
		if palavra[i] == palavra[i+1] and palavra[i] == '.':
			pontos += 1
	return pontos

pontos = countdots()

for i in xrange(q):
	posicao, sub = raw_input().split()
	posicao = int(posicao) - 1
	rm = palavra[posicao]
	palavra[posicao] = sub
	
	if len(palavra) == 1:
		print 0
		continue
	
	if (rm == '.' and sub == '.') or (rm != '.' and sub != '.'):
		print pontos
		continue
		
	if sub == '.': 
		if posicao > 0 and palavra[posicao-1] == '.': pontos += 1
		if posicao < len(palavra)-1 and palavra[posicao+1] == '.': pontos += 1
		print pontos
		continue
	
	if posicao > 0 and palavra[posicao-1] == '.': pontos -= 1
	if posicao < len(palavra)-1 and palavra[posicao+1] == '.': pontos -= 1
	
	print pontos
