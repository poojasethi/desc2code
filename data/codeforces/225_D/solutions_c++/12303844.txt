#include <iostream>
#include <queue>
#include <map>
#define max(a,b) ((a)>(b)?(a):(b))
using namespace std;
struct point
{
	int x,y;
};
char mp[16][16];
int n,m,k,ans;
const int dx[5]={0,0,0,1,-1},dy[5]={0,1,-1,0,0};
map<int,int> vst;
class state
{
public:
	point sn[11];
	state()
	{
	}
	int hash()
	{
		int i,rec=0;
		for (i=1;i<=k;i++)
		{
			rec=rec*171+sn[i].x;
			rec=rec*171+sn[i].y;
		}
		return rec;
	}
	void move(queue<state>& q)
	{
		int i,j;
		state gen;
		for (i=1;i<k;i++)
			gen.sn[i+1]=sn[i];
		for (i=1;i<=4;i++)
		{
			int ox=sn[1].x+dx[i],oy=sn[1].y+dy[i];
			if (ox>0&&ox<=n&&oy>0&&oy<=m&&mp[ox][oy]!='#')
			{
				for (j=2;j<k;j++)
					if (sn[j].x==ox&&sn[j].y==oy)
						break;
				if (j==k)
				{
					gen.sn[1].x=ox;
					gen.sn[1].y=oy;
					int h=gen.hash();
					if (mp[ox][oy]=='@')
					{
						ans=vst[hash()]+1;
						return;
					}
					if (vst.find(h)==vst.end())
					{
						q.push(gen);
						vst[h]=vst[hash()]+1;
					}
				}
			}
		}
	}
};
int main()
{
	int i,j;
	char x;
	state ord;
	queue<state> q;
	cin>>n>>m;
	for (i=1;i<=n;i++)
		for (j=1;j<=m;j++)
		{
			cin>>x;
			if (x=='#'||x=='@'||x=='.')
				mp[i][j]=x;
			else
			{
				k=max(k,x-'0');
				mp[i][j]='.';
				ord.sn[x-'0'].x=i;
				ord.sn[x-'0'].y=j;
			}
		}
	q.push(ord);
	vst[ord.hash()]=0;
	while (!q.empty())
	{
		state f=q.front();
		q.pop();
		f.move(q);
		if (ans)
		{
			cout<<ans;
			return 0;
		}
	}
	cout<<-1;
	return 0;
}
