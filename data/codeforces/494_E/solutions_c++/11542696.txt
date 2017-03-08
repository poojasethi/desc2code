#include <cstdio>
#include <algorithm>
using namespace std;

#define n	100005
#define m	3000005
#define min(a,b)	((a)<(b)?(a):(b))

int		N,M,K,D,_,Rt,Ans;
struct	Lin{int k,l,r,t;}E[n];
struct	Nod{int ls,rs,l,r,sum,laz;}T[m];

inline	bool	Cmp(Lin a,Lin b){return	a.k<b.k;}
inline	void	Up(int u){
		if	(T[u].laz)	T[u].sum=T[u].r^(T[u].l-1);
			else	T[u].sum=T[T[u].ls].sum^T[T[u].rs].sum;
}

inline	void	Modify(int&u,int l,int r,int x,int y,int k){
		if	(!u)	u=++D,T[u].l=l,T[u].r=r;
		if	(x<=l&&r<=y){T[u].laz+=k;Up(u);return;}
		int Mid=l+r>>1;
		if	(x<=Mid)Modify(T[u].ls,l,Mid,x,y,k);
		if	(y>Mid)	Modify(T[u].rs,Mid+1,r,x,y,k);	Up(u);
}

inline	void	Calc(int l,int r){
		for	(int i=0;i<30;i++){
			int x=((r^l-1)>>i)&1,y=(T[Rt].sum>>i)&1;
			if	(x&&y){
				Ans^=min(_,1<<i);
				if	(i)	Ans^=min(_,1<<i-1);
			}
		}
}

int		main(){
		scanf("%d%d%d",&N,&M,&K);
		for	(_=1;_<=K;_<<=1);	_>>=1;
		for	(int i=1,x1,y1,x2,y2;i<=M;i++){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			E[i*2-1]=(Lin){x1,y1,y2,1};
			E[i*2]=(Lin){x2+1,y1,y2,-1};
		}	M*=2;	sort(E+1,E+M+1,Cmp);
		for	(int i=1;i<=M;i++){
			if	(i>1&&E[i].k!=E[i-1].k)	Calc(E[i-1].k,E[i].k-1);
			Modify(Rt,1,N,E[i].l,E[i].r,E[i].t);
		}	puts(Ans?"Hamed":"Malek");
}