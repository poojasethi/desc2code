#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<climits>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<deque>
#include<set>
#include<map>
using namespace std;

#define N 1100

int n,k,pos;
int c[N],t[N],key[N],id[N];

double ans,che;

inline int min(const double &x,const double &y){ return (x<y)?x:y; }

int cmp(const int &x,const int &y){ return (t[x]!=t[y])?t[x]<t[y]:c[x]>c[y]; }

void work(){
	for(int i=0;i<n;i++){id[i]=i;key[i]=i+1;
		scanf("%d%d",&c[i],&t[i]);
	}
	sort(id,id+n,cmp);pos=0;ans=0.0;che=1234567890.0;
	for(int i=0;i<k-1;i++){
		if(t[id[pos]]==1)
			ans+=((double)c[id[pos]])*0.5;
		else ans+=(double)c[id[pos]];
		pos++;
	}
	for(int i=pos;i<n;i++){ che=min(che,c[id[i]]);ans+=c[id[i]]; }
	if(t[id[pos]]==1)ans-=che*0.5;
	printf("%.1f\n",ans);
	for(int i=0;i<k-1;i++){
		printf("1 %d\n",key[id[i]]);
	}
	printf("%d",n-pos);
	for(int i=pos;i<n;i++)printf(" %d",key[id[i]]);
	printf("\n");
}

int main(){
	while(scanf("%d%d",&n,&k)!=EOF)
		work();
	return 0;
}
