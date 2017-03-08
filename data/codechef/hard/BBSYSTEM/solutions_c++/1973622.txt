#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#pragma comment(linker, "/STACK:266777216")
using namespace std;
 
typedef long long LL;
typedef unsigned long ULL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef pair<double,double> PDD;
 
const int inf=1000000000;
//const LL INF=LL(inf)*inf;
const double eps=1e-9;
const double PI=2*acos(0.0);
#define bit(n) (1<<(n))
#define bit64(n) ((LL(1))<<(n))
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) (a).begin(),(a).end()
#define fill(ar,val) memset((ar),(val),sizeof (ar))
#define MIN(a,b) {if((a)>(b)) (a)=(b);}
#define MAX(a,b) {if((a)<(b)) (a)=(b);}
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define sqr(x) ((x)*(x))
#define X first
#define Y second
 
//clock_t start=clock();
//fprintf(stderr,"time=%.3lfsec\n",0.001*(clock()-start));
 
#define D 1111
#define MOD 500009
#define N 2230000
int minp[N];
char deg[N];
short d[N];
int num[D]={0};
int ans[N];
 
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
#endif
	int i,j;
	for(i=2;(j=i*i)<N;i++) if(!minp[i])
		for(;j<N;j+=i) if(!minp[j]) minp[j]=i;
	d[1]=1;
	deg[1]=1;
	for(i=2;i<N;i++)
	{
		int &p=minp[i];
		if(!p) p=i;
		int j=i/p;
		if(minp[j]!=p)
		{
			deg[i]=2;
			d[i]=deg[j]*d[j];
		}
		else
		{
			deg[i]=deg[j]+1;
			d[i]=d[j];
		}
	}
	ans[0]=1;
	for(i=1;i<N;i++)
		ans[i]=LL(++num[deg[i]*d[i]])*ans[i-1]%MOD;
	int T;
	for(scanf("%d",&T);T--;)
	{
		scanf("%d",&i);
		MIN(i,N-1);
		printf("%d\n",(ans[i]+MOD-1)%MOD);
	}
	return 0;
} 