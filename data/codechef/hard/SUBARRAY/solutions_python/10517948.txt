import sys
 
for __ in range(input()) :
	n = input()
	ch = raw_input()
	ops = {')':'(','}':'{',']':'[','>':'<'}
	cls = ['}',')','>',']']
	lists = map(int,sys.stdin.readline().split())
	dp , res , temp = [0]*(n+1) , 0 , 0
	for j,i in enumerate(lists) :
		dp[j] = dp[j-1]+i
	par_st , max_pr , is_empty = [] , [-1]*(n+1) , 0
	for j,i in enumerate(ch) :
		if is_empty :
			if i in cls and ch[par_st[-1]] == ops[i] :
				max_pr[j] = par_st.pop()
				is_empty -= 1
			else :
				is_empty += 1
				par_st.append(j)
		else :
			is_empty += 1
			par_st.append(j)
	ans = [0]*(n+1)
	for i,j in enumerate(lists) :
		if max_pr[i]!=-1 :
			ans[i] = max(dp[i] - dp[max_pr[i]-1]+ans[max_pr[i]-1],ans[i])
	
	print max(ans)