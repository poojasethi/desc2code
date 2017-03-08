inp,ans,ph=set(raw_input()),['sad','happy'],set('iloveyou')
print ans[len(inp.intersection(ph)) == len(ph)]