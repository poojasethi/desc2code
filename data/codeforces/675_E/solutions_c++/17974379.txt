#include<bits/stdc++.h>
#define LL long long
using namespace std;
inline void splay(LL &v){
    v=0;char c=0;int p=1;
    while(c<'0' || c>'9'){if(c=='-')p=-1;c=getchar();}
    while(c>='0' && c<='9'){v=(v<<3)+(v<<1)+c-'0';c=getchar();}
    v*=p;
}
LL q[200010],head=100001,tail=100000;
LL a[100010],n;LL ans,dp[100010];
int main(){
	splay(n);
	for(int i=1;i<n;i++)splay(a[i]);
	q[--head]=n-1;dp[n-1]=1;
	for(int i=n-2;i>=1;i--){
		int x=upper_bound(q+head,q+tail+1,a[i])-q-1;
		dp[i]=n-i+dp[q[x]]-(a[i]-q[x]);
		while(head<=tail&&a[i]>=a[q[head]])++head;
		q[--head]=i;ans+=dp[i];
	}
	cout<<ans+1<<endl;
}