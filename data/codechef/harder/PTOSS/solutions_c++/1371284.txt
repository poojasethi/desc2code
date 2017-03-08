#include"stdio.h"
#include"vector"
#include"set"
#include"map"
#include"assert.h"
#include"algorithm"
#include"math.h"
#include"stdlib.h"
#include"string.h"
#include"string"
using namespace std;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef const int& ci;
typedef const unsigned int& cui;
typedef const long long& cll;
typedef const unsigned long long& cull;
#define REP(i,n) for(unsigned int i=0;i<(n);i++)
#define LOOP(i,x,n) for(int i=(x);i<(n);i++)
#define ALL(v) v.begin(),v.end()
#define FOREACH(it,v)   for(typeof((v).begin()) it=(v).begin();it != (v).end();it++)
#define i(x) scanf("%d",&x)
#define u(x) scanf("%u",&x)
#define l(x) scanf("%l64d",&x)
#define ul(x) scanf("%l64u",&x)
#define P 1000000007
char first[500000],second[500000];
void convert(bool* b,char* a){
	int i=0;
	while(a[0]){
		int str=(a[0]-'a');
		if(a[0]<'a')str=26+a[0]-'A';
		b[i++]=str&16;
		b[i++]=str&8;
		b[i++]=str&4;
		b[i++]=str&2;
		b[i++]=str&1;
		a++;
	}
}
bool s1[1000010],s2[1000010];
int fallback[1000010];
int soln[1000010];
int main(){
	ui T;
	u(T);
	while(T--){
		int n,m;
		scanf("%d%s",&n,first);
		scanf("%d%s",&m,second);
		convert(s1,first);
		convert(s2,second);
		fallback[0]=-1;
		for(int i=1;i<n;i++){
			fallback[i]=fallback[i-1];
			while(fallback[i]>=0 && s1[fallback[i]+1]!=s1[i])
				fallback[i]=fallback[fallback[i]];
			if(s1[fallback[i]+1]==s1[i])fallback[i]++;
		}
//		REP(i,n)printf("s1[%d]=%d\n",i,s1[i]?1:0);
		bool seen=0;int best=-1;
		for(int j=0;j<m;j++){
			while(best>=0 && s1[best+1]!=s2[j])best=fallback[best];
			if(s1[best+1]==s2[j])best++;
			if(best==n-1){seen=1;break;}
//			printf("%d: best=%d\n",j,best);
		}
//		REP(i,m)printf("s2[%d]=%d\n",i,s2[i]?1:0);
		int soln[n+1];
		soln[0]=2;
//		printf("soln[0]=%d\n",soln[0]);
		for(int i=1;i<n;i++){
			int fb=fallback[i-1];
			while(fb>=0 && s1[fb+1]==s1[i])fb=fallback[fb];
			if(s1[fb+1]!=s1[i])fb++;
			soln[i]=2+soln[i-1]+soln[i-1]-(fb>=0?soln[fb]:0);
			while(soln[i]>=P)soln[i]-=P;
			while(soln[i]<0)soln[i]+=P;
//			printf("soln[%d]=%d, fallback= %d\n",i,soln[i],fb);
		}
//		printf("%d\n",best);
		ull ans=seen?0:(soln[n-1]-(best>=0?soln[best]:0)+P)%P;
		printf("%Lu\n",ans);
	}
}
