from math import log

def calculateExp(x, y, z, k):
	if(k == 1):
		return x**(y**z), "x^y^z"
	elif(k == 2):
		return x**(z**y), "x^z^y"
	elif(k == 3 or k == 4):
		return x**(z*y), "(x^y)^z"
	elif(k == 5):
		return y**(x**z), "y^x^z"
	elif(k == 6):
		return y**(z**x), "y^z^x"
	elif(k == 7 or k == 8):
		return y**(x*z), "(y^x)^z"
	elif(k == 9):
		return z**(x**y), "z^x^y"
	elif(k == 10):
		return z**(y**x), "z^y^x"
	elif(k == 11 or k == 12):
		return z**(x*y), "(z^x)^y"

def calculateLogLog(x, y, z, k):
	if(x > 1):
		if(k == 1):
			return z * log(y) + log(log(x)), "x^y^z"
		elif(k == 2):
			return y * log(z) + log(log(x)), "x^z^y"
		elif(k == 3 or k == 4):
			return log(y) + log(z) + log(log(x)), "(x^y)^z"

	if(y > 1):
		if(k == 5):
			return z * log(x) + log(log(y)), "y^x^z"
		elif(k == 6):
			return x * log(z) + log(log(y)), "y^z^x"
		elif(k == 7 or k == 8):
			return log(x) + log(z) + log(log(y)), "(y^x)^z"

	if(z > 1):
		if(k == 9):
			return y * log(x) + log(log(z)), "z^x^y"
		elif(k == 10):
			return x * log(y) + log(log(z)), "z^y^x"
		elif(k == 11 or k == 12):
			return log(x) + log(y) + log(log(z)), "(z^x)^y"

	return False, ""
def getAns(x, y, z):
	if(max(x,y,z) < 1):
		maxNum, ans = 0, ""
		for i in index:
			t = calculateExp(x, y, z, i)
			if(t[0] > maxNum):
				ans = t[1]
				maxNum = t[0]
		return ans
	elif(max(x, y, z) == 1):
		if(x == 1):
			return "x^y^z"
		elif(y == 1):
			return "y^x^z"
		else:
			return "z^x^y"
	else:
		maxNum, ans = None, ""
		for i in index:
			t = calculateLogLog(x, y, z, i)
			if(t[0] != False):
				if(maxNum == None or t[0] > maxNum):
					ans = t[1]
					maxNum = t[0]
			# print(t, ans)

		return ans

index = [1, 2, 3, 5, 6, 7, 9, 10, 11]
if(__name__ == "__main__"):
	x, y, z = [float(t) for t in raw_input().split(' ')]
	
	print(getAns(x, y, z))