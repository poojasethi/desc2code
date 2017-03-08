#define _CRT_SECURE_NO_DEPRECATE
#include<stdio.h>
#include<cstring>
#include<math.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<vector>
#include<iostream>
#include <cctype>
char str[105];
int check(int a, int b) {
	for (int i = a; i < b; ++i)
		if (!isalpha(str[i]) && !isdigit(str[i]) && str[i] != '_') return 0;
	if (b - a > 16 || a == b) return 0;
	return 1;
}
int judge() {
	int tmp = -1, l = strlen(str);
	for (int i = 0; i < l; ++i)
		if (str[i] == '@') {
			if (tmp != -1) return 0;
			tmp = i;
		}
	if (tmp == -1) return 0;
	if (!check(0, tmp)) return 0;
	int p = tmp + 1, f = tmp;
	while (f < l && str[f] != '/') f++;
	if (f < l && !check(f + 1, l)) return 0;
	if (f - p > 32 || f - p == 0) return 0;
	str[f] = '.';
	for (int i = tmp + 1; i <= f; ++i)
		if (str[i] == '.') {
			if (!check(p, i)) return 0;
			p = i + 1;
		}
	return 1;
}
int main() {
	while (scanf("%s", str) != EOF)
		if (judge()) printf("YES\n"); 
		else
			printf("NO\n");
	return 0;
}