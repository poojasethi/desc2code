#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#define ll long long
using namespace std;
const int maxn= 2e5;
char s[maxn];
int a[maxn];
int n,l,r,i,x;
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%s",s+1);
	n= strlen(s+1);
	for (i= 1;i<=n;i++)
		a[i]= s[i]-'0';
	l= 1;r= n;
	if (a[l]!=a[r]){
		a[l]--;
		a[l+1]+= 10;
		if (!a[l]) l++;
		else if (a[l]!=a[r]){
			printf("0");
			return 0;
		}
	}
	while (l<=r){
		if (a[l]>=a[r]+10&&a[r]<10)
			a[r-1]--,a[r]+= 10;
		if (a[l]==a[r]+1)
			a[l+1]+= 10,a[l]--;
		if (a[l]!=a[r])
			break;
		if (l!=r){
			a[l]= a[l]-a[l]/2;
			a[r]-= a[l];
		}else if ((a[l]&1)==0)
			a[l]>>= 1;
		else break;
		if (a[l]<0||a[l]>9||a[r]<0||a[r]>9) break;
		l++;
		r--;
	}
	if (l<=r){
		printf("0");
	}else {
		l= 1;
		if (!a[l]) l++;
		while (l<=n){
			printf("%d",a[l]);
			l++;
		}
	}return 0;
}
