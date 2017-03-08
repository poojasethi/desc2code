#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>

using namespace std;

#define MOD 1000000007
#define inf 2147483647
#define ninf -2147483648
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define s(a) scanf("%d",&a)
#define sll(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define p(a) printf("%d",a)
#define pll(a) printf("%lld",a)
#define ps(a) printf("%s",a)
#define pc(a) printf("%c",a)
#define nline printf("\n")
#define space printf(" ")
#define ll long long

void multiply(long long int a[][15],long long int b[][15]){
	long long int c[15][15]={0},i,j,k;

	for(i=0;i<15;++i){
		for(j=0;j<15;++j){
			for(k=0;k<15;++k){
				if(a[i][k]>MOD)
					a[i][k]%=MOD;

				if(b[k][j]>MOD)
					b[k][j]%=MOD;

				c[i][j]+=a[i][k]*b[k][j];

				if(c[i][j]>MOD)
					c[i][j]%=MOD;
			}
		}
	}
	
	for(i=0;i<15;++i)
		for(j=0;j<15;++j)
			a[i][j]=c[i][j];
}

void matr(long long int a[][15], long long int n){
	long long int c[15][15],i,j;

	if(n==2){
		multiply(a,a);
	}
	else if(n==1){
		return;
	}
	else{
		if(n&1){//odd
			for(i=0;i<15;++i)
				for(j=0;j<15;++j)
					c[i][j]=a[i][j];

			matr(a,n/2);
			multiply(a,a);
			multiply(a,c);
		}
		else{
			matr(a,n/2);
			multiply(a,a);
		}
	}
}

int main() {
	int test, val, n;
	ll int l;
	s(test);
	while(test--){
		ll int a[15][15] = {0};
		sll(l);
		s(n);
		FOR(i, 0, n){
			s(val);
			++a[0][val-1];
		}
		for(int i=1;i<15;++i){
			++a[i][i-1];
		}
		matr(a, l);
		printf("%lld\n", a[0][0]);
	}
	return 0;
}