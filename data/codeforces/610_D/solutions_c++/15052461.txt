#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;
typedef long long ll;
const int INF=0x3f3f3f3f;
const int mod=1e9+7;
const int maxn=4e5+5;

struct seg{
	ll y1,y2,x,c;
	bool operator < (const seg a)const{
		return x<a.x;
	}
}s[maxn];

ll cov[maxn<<2];
ll y[maxn],st[maxn<<2];

void pushup(int o,int l,int r){
	if(cov[o]>0)st[o]=y[r]-y[l];
	else if(cov[o]==0){
		if(l+1==r)st[o]=0;
		else st[o]=st[o<<1]+st[o<<1|1];
	}
}

void update(int o,int l,int r,seg a){
	if(a.y1<=y[l]&&a.y2>=y[r]){
		cov[o]+=a.c;
		pushup(o,l,r);
		return;
	}
	if(l+1==r)return;
	int m=l+((r-l)>>1);
	if(a.y1<y[m])update(o<<1,l,m,a);
	if(a.y2>y[m])update(o<<1|1,m,r,a);
	pushup(o,l,r);
}

int main(){
	int n;
	scanf("%d",&n);
	memset(st,0,sizeof(st));
	memset(cov,0,sizeof(cov));
	ll ans=0;
	for(int i=1;i<=n;++i){
		ll x1,y1,x2,y2;
		scanf("%I64d%I64d%I64d%I64d",&x1,&y1,&x2,&y2);
		if(x1==x2){
			if(y1>y2)swap(y1,y2);
		}
		else if(y1==y2){
			if(x1>x2)swap(x1,x2);
		}
		x2++;
		y2++;
		s[2*i-1].x=x1;s[2*i-1].y1=y1;s[2*i-1].y2=y2;s[2*i-1].c=1;
		y[2*i-1]=y1;
		s[2*i].x=x2;s[2*i].y1=y1;s[2*i].y2=y2;s[2*i].c=-1;
		y[2*i]=y2;
	}
	sort(y+1,y+2*n+1);
	sort(s+1,s+2*n+1);
	int cnt=1;
	for(int i=2;i<=2*n;++i){
		if(y[i]!=y[i-1])y[++cnt]=y[i];
	}
	for(int i=1;i<2*n;++i){
		update(1,1,cnt,s[i]);
		ans+=st[1]*(s[i+1].x-s[i].x);
	}
	printf("%I64d\n",ans);
	return 0;
}
