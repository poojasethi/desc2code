
test_cases = int(raw_input())
while(test_cases):
	numbers = raw_input().split()
	first = numbers[0]
	second = numbers[1]
	#reverse the input strings and convert into number
	first_reverse = int(first[::-1])
	second_reverse = int(second[::-1])
	#sum of the reversed strings and add
	solution = first_reverse + second_reverse
	#convert the solution into string
	solution_string = str(solution)
	#print thereversed solution
	solution_string = solution_string[::-1]
	print int(solution_string)
	test_cases-=1
