#include <stdio.h>
#include <algorithm>

#define if if (
#define then )
#define do )
#define for for (
#define while while (
#define begin {
#define end }

#define M 131072

#define MAXN 100005

char ch;
inline void read(int &x)
begin
	x=0;ch=getchar();
	while ch<=32 do ch=getchar();
	while ch>32 do begin
		x=x*10+ch-48;ch=getchar();
	end;
end;

struct segtree begin
	int tr[M*2];
	
	inline void mod(int l,int r,int val)
	begin
		if l>r then return;
		l+=M-1;r+=M+1;
		while l^r^1 do begin
			if ~l&1 then tr[l^1]+=val;
			if r&1 then tr[r^1]+=val;
			l>>=1;r>>=1;
		end;
	end;
	
	inline int que(int x)
	begin
		int ret=0;
		x+=M;
		while x do begin
			ret+=tr[x];
			x>>=1;
		end;
		return ret;
	end;
end;

segtree T1,T2;

int n,Q;

int a[MAXN];

struct que begin
	int l,r,id;
end;

inline bool operator < (que a,que b)
begin
	return a.r<b.r;
end;

que q[MAXN];
int ans[MAXN];

int last[MAXN];
int last2[MAXN];
int dist[MAXN];
int first[MAXN];

int main()
begin
	read(n);
	int i;
	for i=1;i<=n;i++ do begin
		read(a[i]);
	end;
	read(Q);
	for i=1;i<=Q;i++ do begin
		int l,r;
		read(l);read(r);
		q[i]=(que){l,r,i};
	end;
	std::sort(q+1,q+Q+1);
	q[Q+1].r=1000000000;
	int j=1;
	for i=1;i<=n;i++ do begin
		int x=a[i];
		T1.mod(last[x]+1,i,1);
		if !first[x] then first[x]=1;
		T2.mod(last[x]+1,i,1);
		if dist[x]!=i-last[x] then begin
			T2.mod(first[x],last2[x],-1);
			first[x]=last2[x]+1;
			dist[x]=i-last[x];
		end;
		last2[x]=last[x];
		last[x]=i;
		while q[j].r==i do begin
			ans[q[j].id]=T1.que(q[j].l)+(T2.que(q[j].l)==0);
			++j;
		end;
	end;
	for i=1;i<=Q;i++ do begin
		printf("%d\n",ans[i]);
	end;
end