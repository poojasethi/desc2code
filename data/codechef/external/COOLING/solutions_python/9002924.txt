for i in range(int(raw_input())):
	count = 0;
	num = int(raw_input())
	pieWt = map(int, raw_input().split())
	racksWt = map(int, raw_input().split())
	for i in range(0,len(pieWt)):
		if max(pieWt) <= max(racksWt):
			count += 1
			pieWt.remove(max(pieWt))
			racksWt.remove(max(racksWt))
		else:
			pieWt.remove(max(pieWt))
	print count
