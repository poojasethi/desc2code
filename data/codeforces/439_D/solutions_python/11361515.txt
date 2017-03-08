## Author: Gilberto A. dos Santos
## Website: http://codeforces.com/problemset/problem/439/D

n, m = map(int, raw_input().split(" "))

a = map(int, raw_input().split(" "))
b = map(int, raw_input().split(" "))

a.sort(reverse=True)
b.sort()

ans = 0
while a and b and a[-1] < b[-1]:
    ans += b.pop() - a.pop()
print ans
