#include <cstdio>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#define X 1000000001
#define N 100101

using namespace std;
int n,m;

struct node{ int l,r;
	node(int ll,int rr){ l=min(ll,rr),r=max(ll,rr); }
};

struct segment{ int i,l;
	segment(int id,int ll){ i=id,l=ll; }
};

map<int,vector<node> > xv,yv;
map<int,vector<node> >::iterator it;
int cmp(node a,node b){ return a.l==b.l?a.r<b.r:a.l<b.l; }
vector<segment> seg;

inline int B(int i){ return 1<<i; }

void getid(int &id,map<int,vector<node> > v)
{
	for(;;id++)
		if(v.count(id)==0)
			break;
}

void gao(int n,int m,map<int,vector<node> > v,int &ret,int add)
{
	for(it=v.begin(); it!=v.end(); it++)
	{
		int i=it->first;
		sort(v[i].begin(),v[i].end(),cmp);
		int l=0,r=0;
		int len=0;
		for(int j=0; j<v[i].size(); j++)
		{
			int x=v[i][j].l,y=v[i][j].r;
			if(x>r)
			{
				len+=x-r;
				l=x,r=y;
			}
			else if(y>r)
				r=y;
		}
		if(r<m)
			len+=m-r;
		seg.push_back(segment(i+add,len));
		ret^=len;
	}
	if(v.size()<n-1)
	{
		int id=1;
		if(n-1-v.size()>=2)
		{
			getid(id,v);
			seg.push_back(segment(id+add,m));
			id++;
			getid(id,v);
			seg.push_back(segment(id+add,m));
			id++;
		}
		if((n-1-v.size())&1)
		{
			getid(id,v);
			seg.push_back(segment(id+add,m));
			ret^=m;
		}
	}
}

int main()
{
	int k;
	scanf("%d%d%d",&n,&m,&k);
	for(int i=0; i<k; i++)
	{
		int x1,y1,x2,y2;
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		if(x1==x2)
			xv[x1].push_back(node(y1,y2));
		else
			yv[y1].push_back(node(x1,x2));
	}
	int ret=0;
	gao(n,m,xv,ret,0);
	gao(m,n,yv,ret,X);

	if(ret>0)
	{
		puts("FIRST");
		int wei=0,now=0,nid=0;
		for(wei=30; wei>=0; wei--)
			if(ret&B(wei))
				break;
		for(int i=0; i<seg.size(); i++)
		{
			if((seg[i].l)&B(wei))
			{
				now=seg[i].l;
				nid=seg[i].i;
				break;
			}
		}
		//printf("%d %d %d %d\n",ret,now,ret^now,nid);
		int ans=now-(ret^now),l,r,tl;
		if(nid>=X)
		{
			nid-=X;
			printf("%d %d ",0,nid);
			sort(yv[nid].begin(),yv[nid].end(),cmp);
			l=r=tl=0;
			for(int i=0; i<yv[nid].size(); i++)
			{
				int x=yv[nid][i].l,y=yv[nid][i].r;
				if(x>r)
				{
					tl+=x-r;
					l=x,r=y;
				}
				else if(y>r)
					r=y;
				if(tl>=ans)
				{
					printf("%d %d\n",l-(tl-ans),nid);
					break;
				}
			}
			if(tl<ans)
				printf("%d %d\n",ans-tl+r,nid);
		}
		else
		{
			printf("%d %d ",nid,0);
			sort(xv[nid].begin(),xv[nid].end(),cmp);
			l=r=tl=0;
			for(int i=0; i<xv[nid].size(); i++)
			{
				int x=xv[nid][i].l,y=xv[nid][i].r;
				if(x>r)
				{
					tl+=x-r;
					l=x,r=y;
				}
				else if(y>r)
					r=y;
				if(tl>=ans)
				{
					printf("%d %d\n",nid,l-(tl-ans));
					break;
				}
			}
			if(tl<ans)
				printf("%d %d\n",nid,ans-tl+r);
		}
	}
	else
		puts("SECOND");
	return 0;
}
