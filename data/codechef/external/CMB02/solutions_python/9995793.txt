def palindrome(x):
    n = str(x)
    str1 = ''
    for i in range(len(n)-1,-1,-1):
        str1 += n[i]
    if str1 == n:
        return True
    else:
        return False

a = input()
for h in range(a):
    num = input() + 1
    while palindrome(num) != True:
        num += 1
    print num