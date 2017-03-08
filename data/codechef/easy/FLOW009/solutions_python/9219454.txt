lineAmount = int(raw_input())
result = 0
i = 0

while i < lineAmount:
	userData = raw_input()
	splitUserData = userData.split(" ")
	productsAmount = int(splitUserData[0])
	#print "products " + str(productsAmount)
	price = int(splitUserData[1])
	#print "price " + str(price)

	result = productsAmount * price
	if productsAmount > 1000:
		print "%.6f" % (result * 0.9)
	else:
		print "%.6f" % result 
	i+= 1
	