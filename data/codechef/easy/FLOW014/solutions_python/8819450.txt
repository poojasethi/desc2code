t = int(raw_input())
grade = []
for i in range(0,t):
	hard,carbon,tensile = map(float,raw_input().split())
	hard = int(hard)
	tensile = int(tensile)
	if hard > 50 and carbon < 0.7 and tensile > 5600:
		grade.append(10)
	elif hard > 50 and carbon < 0.7:
		grade.append(9)
	elif carbon < 0.7 and tensile > 5600:
		grade.append(8)
	elif hard > 50 and tensile > 5600:
		grade.append(7)
	elif hard > 50 or carbon < 0.7 or tensile > 5600:
		grade.append(6)
	else:
		grade.append(5)
for i in grade:
	print i
