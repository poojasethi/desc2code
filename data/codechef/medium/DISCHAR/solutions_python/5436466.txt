import sys
def main():

	t = sys.stdin.readline()
	t = int(t)
	while(t):
		s = sys.stdin.readline()
		uniqueWords = [] 
		for i in s:
		      if not i in uniqueWords:
		          uniqueWords.append(i);
		print len(uniqueWords)-1
		t=t-1

if __name__ == "__main__":
    main()