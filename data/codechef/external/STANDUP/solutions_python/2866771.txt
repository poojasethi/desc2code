#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <stack>
#include <vector>
#include <map>
#include <list>
#include <queue>
#define lli long long int
#define ii pair<long long int,long long int>

#define mod 1000000007
#define inf 999999999
#define eps 1e-7
using namespace std;

inline void inp(lli &n ) {//fast input function
	n=0;
	lli ch=getchar_unlocked(),sign=1;
	while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getchar_unlocked();}
	while( ch >= '0' && ch <= '9' )
		n=(n<<3)+(n<<1)+ ch-'0', ch=getchar_unlocked();
	n=n*sign;
}
double ans[2501][2501];

double fun(int n,int k) {
	// cout<<n<<" "<<k<<" "<<ans[n][k]<<endl;
	if(n==0)
		return 0;

	if(n==k)
		return n;
	if(k>n)
		return 0;
	// cout<<"dude\n";
	if(ans[n][k])
		return ans[n][k];
	// cout<<"dude\n";
	double num=0,val;

	if(k) {
		num=(double)k/(double)n;
		num=num*(1.0+fun(n-1,k-1));
	}

	val=(double)(n-k)/(double)(n);

	val*=(double)(n-k-2)/(double)(n-1);

	num+=val*(1+fun(n-2,k+2));

	val=(double)(k)/(double)(n-1);
	val*=(double)(n-k)/(double)(n);

	num+=val*(2+fun(n-2,k));

	val=1.0/(double)(n-1);
	val*=(double)(n-k)/(double)(n);

	num+=val*(1+fun(n-2,k));

	ans[n][k]=num;
	return num;
}

int main() {
	int n,m;

	memset(ans,0,sizeof ans);


	while(scanf("%d %d",&n,&m)!=EOF) {
		printf("%.4f\n", fun(n*m,0));
	}

	return 0;
}