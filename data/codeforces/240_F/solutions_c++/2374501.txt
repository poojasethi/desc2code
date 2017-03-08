#include <cstdio>
#define N 100011
#define X 26

struct node{ int l,r,c,a;
	int gm(){ return (l+r)>>1; }
	int len(){ return r-l+1; }
};

inline int L(int i){ return i<<1; }
inline int R(int i){ return i<<1|1; }

int cnt[X];

struct segment
{
	node no[N<<2];
	void init(int id,int l,int r)
	{
		no[id].l=l,no[id].r=r,no[id].c=0,no[id].a=0;
		if(l==r) return;
		init(L(id),l,no[id].gm());
		init(R(id),no[id].gm()+1,r);
	}

	void down(int id)
	{
		int x=no[id].a;
		if(x>=0)
		{
			no[L(id)].a=x;
			no[R(id)].a=x;
			no[L(id)].c=x*no[L(id)].len();
			no[R(id)].c=x*no[R(id)].len();
			no[id].a=-1;
		}
	}

	void update(int id,int ll,int rr,int x)
	{
		int l=no[id].l,r=no[id].r,m=no[id].gm();
		if(l>=ll&&r<=rr)
		{
			no[id].a=x;
			no[id].c=x*no[id].len();
			return;
		}
		down(id);
		if(m>=ll&&l<=rr)
			update(L(id),ll,rr,x);
		if(m<rr&&r>=ll)
			update(R(id),ll,rr,x);
		no[id].c=no[L(id)].c+no[R(id)].c;
	}

	int query(int id,int ll,int rr)
	{
		int l=no[id].l,r=no[id].r,m=no[id].gm();
		if(l>=ll&&r<=rr)
			return no[id].c;
		down(id);
		int ret=0;
		if(m>=ll&&l<=rr) 
			ret+=query(L(id),ll,rr);
		if(m<rr&&r>=ll)
			ret+=query(R(id),ll,rr);
		return ret;
	}
}seg[X];

char s[N];

int ok()
{
	int od=0,ev=0;
	for(int i=0; i<X; i++)
	{
		if(cnt[i]&1)
			od++;
		else
			ev++;
	}
	return od<=1;
}

int main()
{
	int n,m;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	while(scanf("%d%d",&n,&m)+1)
	{
		scanf("%s",s);
		for(int i=0; i<X; i++)
			seg[i].init(1,1,n);
		for(int i=0; s[i]; i++)
			seg[s[i]-'a'].update(1,i+1,i+1,1);
		for(int i=0; i<m; i++)
		{
			int l,r;
			scanf("%d%d",&l,&r);
			for(int j=0; j<X; j++)
				cnt[j]=seg[j].query(1,l,r);
			if(ok())
			{
				int nl=l,nr=r;
				for(int j=0; j<X; j++)
				{
					seg[j].update(1,l,r,0);
					if(cnt[j]&1)
					{
						int x=cnt[j]>>1,mid=(nl+nr)>>1;
						seg[j].update(1,mid,mid,1);
						seg[j].update(1,nl,nl+x-1,1);
						seg[j].update(1,nr-x+1,nr,1);
						nl=nl+x;
						nr=nr-x;
					}
					else if(cnt[j]>0)
					{
						int x=cnt[j]>>1;
						seg[j].update(1,nl,nl+x-1,1);
						seg[j].update(1,nr-x+1,nr,1);
						nl=nl+x;
						nr=nr-x;
					}
				}
			}
		}
		for(int k=1; k<=n; k++)
		{
			int ii=-1;
			for(int i=0; i<X; i++)
			{
				if(seg[i].query(1,k,k)>0)
				{
					ii=i;
					break;
				}
			}
			s[k-1]=ii+'a';
		}
		s[n]=0;
		printf("%s\n",s);
	}
	return 0;
}
