n = input()
length = map(int, raw_input().split())
print max([length.count(i) for i in length]), len(set(length))
