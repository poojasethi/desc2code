n = int(input())
ans = "-1"
num = n / 7;
for i in range(num, -1, -1):
	if (n - i * 7) % 4 == 0:
		ans = '4' * ((n - i * 7) / 4) + i * '7'
		break;
print ans;
