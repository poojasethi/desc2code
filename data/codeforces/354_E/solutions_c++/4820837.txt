#include<cstdio>
#include<cstring>
typedef long long LL;

LL pow[20];
struct Sta{
	int num[6];
	bool ok;
} S[5][10];
LL ans[6];

bool dfs(LL n,int l) {
	if (!n) return true;
	LL p = pow[l];
	for(int i = 0; i < 5; i++)
		if(n/10-i >= 0 &&
			S[i][n%10].ok
		) {
			for(int k = 0; k < 6; k++)
				ans[k] += S[i][n%10].num[k] * p;
			if(dfs(n/10-i,l+1))
				return true;
			for(int k=0;k<6;k++)
				ans[k] -= S[i][n%10].num[k] * p;
	 	}
	return false;
}

int main() {
	int t;
	LL n;
	scanf("%d",&t);

	for(int i=0;i<5;i++)
		for(int j=0;j<10;j++)
			S[i][j].ok=false;

	for(int i=0;i<=6;i++)
		for(int j=0;j<=6;j++)
			if(i+j<=6) {
				int n1=(i * 4 + j * 7) / 10, n2 = (i * 4 + j * 7)%10;
				S[n1][n2].ok = true;
				for(int k = 0; k < i; k++)
					S[n1][n2].num[k] = 4;
				for(int k = 0; k < j; k++)
					S[n1][n2].num[k+i] = 7;
				for(int k = i + j; k < 6; k++)
					S[n1][n2].num[k] = 0;
			}

	pow[0] = 1;
	for (int i = 1; i <=19; i++)
		pow[i] = pow[i-1] * 10;
	
	while(t--) {
		for(int i=0;i<6;i++)
			ans[i]=0;
		scanf("%I64d",&n);
		if(dfs(n,0)==false)
			puts("-1");
		else {
			for(int i=0;i<6;i++)
				printf("%I64d ",ans[i]);
			puts("");
		}
	}
	return 0;
}