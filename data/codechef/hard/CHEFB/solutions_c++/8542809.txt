/*
Author : lifecodemohit
Problem : https://www.codechef.com/problems/CHEFB
*/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

#define MOD 			1000000007
#define ll 				long long 
#define si(a)			scanf("%d", &a)
#define sn(a)			scanf("%lld", &a)
#define pi(a)			printf("%d\n", a)
#define pn(a)			printf("%lld\n", a)
#define ss(a)			scanf("%s", a)
#define rep(i, s, e)	for (int i = s; i <= e; i++)
#define rrep(i, s, e)	for (int i = s; i >= e; i--)
#define mem(arr, val)	memset(arr, val, sizeof(arr))
#define pb				push_back
#define mp				make_pair

ll cnt [1000010];
ll arr[1000010];

void sieve() {
	for (int i = 2; i <= 1000000; i++)
		arr[i] = i;
	for (int i = 2; i <= 1000000; i++) {
		if (arr[i] == i) { 
			for (int j = i + i; j <= 1000000; j += i)
				arr[j] = i;
		}
	}
}

int main()
{
	sieve();
	int t;
	si(t);
	while (t--) {
		int n, a;
		si(n);
		mem(cnt, 0);
		for (int i = 0; i < n; i++) {
			si(a);
			int j = 0;
			while (a > 1) {
				ll count = 0;
				ll val = arr[a];
				while ((a > 1) && (a % val == 0)) {
					a = a / val;
					count++;
				}
				cnt[val] = max(cnt[val], count);
				j++;
			}
		}
		ll ans = 0;
		for (int i = 0; i <= 1000000; i++)
			ans = ans + cnt[i];
		printf("%lld\n", ans);
	}
	return 0;
}