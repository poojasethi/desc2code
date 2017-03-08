## EUCLIDEAN ALGORITHM used

# Default modulus based implementation of 
# Greatest Common Denominator or Highest Common Factor
def gcd1(a,b):
    while b != 0 :
        t = b
        b = a % b
        a = t
    return a

# Only subtraction and comparison 
def gcd2(a,b):
    while a != b :
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Recursive implementation
def gcd3(a,b):
    if b == 0:
        return a
    else:
        return gcd3(b, a % b)

gcd  = gcd1

T = int(raw_input())

for i in range(T):
    nums = map(int, raw_input().split())
    res = nums[1]
    for j in range(2, nums[0] + 1):
        res = gcd(res, nums[j])
    print ' '.join(map(str, map(lambda x: x/res, nums[1:])))
        
