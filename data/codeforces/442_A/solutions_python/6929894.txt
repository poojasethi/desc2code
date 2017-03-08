from collections import defaultdict

def main():
  	input()
	cards = list(set(raw_input().split()));

	if len(cards) == 1:
	  	print 0
		return
	answer = 9;
	chars = 'RGBYW12345'
	for mask in xrange(1, 1024):
	  	cover = ''
		for i in xrange(10):
		  	if (mask & (1<<i)):
			  	cover += chars[i]

		d = defaultdict(int)
  		
  		for card in cards:
			if card[0] in cover and card[1] in cover:
				continue;
			if card[0] in cover:
				d[card[0]] += 1;
			elif card[1] in cover:
				d[card[1]] += 1;
			else:
				d['*'] += 1;
		
		if all(x <= 1 for x in d.values()):
		  	answer = min(answer, len(cover));
		
	print answer;

if __name__ == '__main__':
	main()
