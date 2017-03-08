
def KMPSearch(pat, txt, M):

	# create lps[] that will hold the longest prefix suffix 
	# values for pattern
	lps = [0]*M
	j = 0 # index for pat[]

	# Preprocess the pattern (calculate lps[] array)
	computeLPSArray(pat, M, lps)

	i = 0 # index for txt[]
	best = 0
	res = 0
	ans = 0
	while i < M:
		if pat[j] == txt[i]:
			i+=1
			j+=1
			best += 1

		if best > res:
			res = best
			ans = i - j

		if j==M:
			break

		# mismatch after j matches
		elif i < M and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
			best = 0 
			if j != 0:
				j = lps[j-1]
			else:
				i+=1
	print ans			

def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i]==pat[len]:
			len+=1
			lps[i] = len
			i+=1
		else:
			if len!=0:
				# This is tricky. Consier the example AAACAAAA
				# and i = 7
				len = lps[len-1]

				# Also, note that we do not increment i here
			else: 
				lps[i] = 0
				i+=1

M = input()
if M <= 0:
	print 0
else:
	pat = raw_input()
	txt = raw_input()
	KMPSearch(pat, txt, M)