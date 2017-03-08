#include <cstdio>
#include <cstring>
#include <vector>
#define N 100010

using namespace std;

int num[N],next[N],id[N],nb[N],ans[N];

vector<int> qr[N];
vector<int> qi[N];

inline int lowbit(int x) { return x&(-x); }

struct bit {
	int arr[N];

	bit() {
		for(int i=0; i<N; i++) {
			arr[i]=0;
		}
	}

	void add(int id,int x) {
		for(; id<N; id+=lowbit(id)) {
			arr[id]+=x;
		}
	}

	int sum(int id) {
		int ret=0;
		for(; id>0; id^=lowbit(id))
		{
			ret+=arr[id];
		}
		return ret;
	}
};

void solve(int n) {
	bit b1,b2;
	for(int i=n; i>=1; i--) {
		b1.add(i,1);
		b1.add(next[i],-1);
		for(int j=0; j<qr[i].size(); j++) {
			int r=qr[i][j],id=qi[i][j];
			ans[id]+=b1.sum(r);
		}
		b2.add(i,1);
		b2.add(nb[i],-1);
		b2.add(next[i],-1);
		b2.add(nb[next[i]],1);
		for(int j=0; j<qr[i].size(); j++) {
			int r=qr[i][j],id=qi[i][j];
			if(b2.sum(r)==0)
				ans[id]++;
		}
	}
}

int main() {
	int n;
	scanf("%d",&n);
	for(int i=1; i<=n; i++) {
		scanf("%d",&num[i]);
	}
	for(int i=0; i<N; i++) {
		id[i]=n+1;
	}
	next[n+1]=n+1;
	for(int i=n; i>=1; i--) {
		next[i]=id[num[i]];
		id[num[i]]=i;
	}
	nb[n+1]=n+1;
	for(int i=n; i>=1; i--) {
		if(next[i]==n+1) {
			nb[i]=n+1;
		}
		if(next[next[i]]==n+1) {
			nb[i]=n+1;
		}
		int x=next[i],y=next[next[i]];
		if(y-x==x-i) {
			nb[i]=nb[x];
		}
		else {
			nb[i]=y;
		}
	}
	int q;
	scanf("%d",&q);
	for(int i=0; i<q; i++) {
		int x,y;
		scanf("%d%d",&x,&y);
		if(y>n) 
			y=n;
		qr[x].push_back(y);
		qi[x].push_back(i);
	}
	memset(ans,0,sizeof(ans));
	solve(n);
	for(int i=0; i<q; i++) {
		printf("%d\n",ans[i]);
	}
	return 0;
}
