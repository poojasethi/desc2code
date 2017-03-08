direction=[-1,1][raw_input()=='L']
row="qwertyuiopasdfghjkl;zxcvbnm,./"
print ''.join([row[row.index(i)+direction] for i in raw_input()])