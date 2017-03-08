t = int(raw_input())
gross_salary = []
for i in range(0,t):
	salary = float(raw_input())
	if salary < 1500:
		salary = salary * 2
		gross_salary.append(salary)
	else:
		salary = salary + 500 + .98 * salary
		gross_salary.append(salary)
for gross in gross_salary:
	print "%g" %gross
