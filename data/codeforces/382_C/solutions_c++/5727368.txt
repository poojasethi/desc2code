#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxn = 100001;

int num[maxn],n;

int main() {
	while(~scanf("%d",&n)) {
		for(int i = 0;i < n;i++) scanf("%d",num + i);
		if(n == 1) {
			printf("-1\n"); continue;
		} else if(n == 0) {
			printf("0\n"); continue;
		}
		sort(num,num + n);
		int d = 2100000000,count = 0,pos = 0;
		for(int i = 0;i < n - 1;i++) if(num[i + 1] - num[i] < d) d = num[i + 1] - num[i];
		for(int i = 0;i < n - 1;i++) if(num[i + 1] - num[i] != d) {
			count++; pos = i;
		}
		if(count == 0) {
			if(n == 2 && d > 1 && (num[0] + num[1]) % 2 == 0) printf("3\n%d %d %d\n",num[0] - d,(num[0] + num[1]) / 2,num[1] + d);
			else if(d != 0){
				printf("2\n%d %d\n",num[0] - d,num[n - 1] + d);
			} else {
				printf("1\n%d\n",num[0]);
			}
		} else if(count == 1 && ((num[pos] + num[pos + 1]) % 2 == 0) && (num[pos] + num[pos + 1]) / 2 - num[pos] == d) {
			printf("1\n%d\n",(num[pos] + num[pos + 1]) / 2);
		} else {
			printf("0\n");
		}
	}
	return 0;
}
