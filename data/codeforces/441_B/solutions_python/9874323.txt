n, v = map(int, raw_input().split())

fruits_list = [0] * 3001

for i in range(n):
	day, fruits = map(int, raw_input().split())	
	
	fruits_list[day] += fruits

total_fruits = 0

for i in range(1, 3001):
	temp_v = v
	
	temp_fruits = fruits_list[i-1]
	
	if temp_fruits > temp_v:
		total_fruits += temp_v
		continue
	else:
		total_fruits += temp_fruits
		temp_v -= temp_fruits
	
	temp_fruits = fruits_list[i]
	if temp_fruits > temp_v:
		total_fruits += temp_v
		fruits_list[i] -= temp_v
	else:
		total_fruits += temp_fruits
		fruits_list[i] = 0
		
last_tree_fruits = fruits_list[-1]

if last_tree_fruits > v:
	total_fruits += v
else:
	total_fruits += last_tree_fruits


print total_fruits
