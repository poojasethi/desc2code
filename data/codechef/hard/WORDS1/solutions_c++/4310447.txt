#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<climits>
#include<sstream>

#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<bitset>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef pair<int,int> pii;
typedef long long int lld;
typedef long double Lf;
typedef unsigned long long int llu;

#define sz(a)                        int((a).size()) 
#define pb                           push_back 
#define mp                           make_pair
#define F                            first
#define S                            second
#define present(c,x)                 ((c).find(x) != (c).end()) 
#define cpresent(c,x)                (find(all(c),x) != (c).end())
#define tr(c,i)                      for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define rtr(c,i)                      for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c)                       (c).begin(),(c).end()
#define si(n)                        inp(n)
#define sl(n)                        scanf("%lld",&n)
#define sf(n)                        scanf("%f",&n)
#define sd(n)                        scanf("%lf",&n)
#define ss(n)                        scanf("%s",n)
#define sii(n,m)		     inp(n);inp(m)
#define siii(n,m,r)		     inp(n);inp(m);inp(r)

#define abs(x)                       ((x)<0?-(x):(x))
#define fill(a,v)                    memset((a),(v),sizeof (a))
#define INF                          INT_MAX
#define LINF                         (long long)1e18
#define EPS                          1e-9
#define MODBY 1000000007
#define MAX     

#define getcx getchar_unlocked
 
inline void inp( int &n )
{
n=0;
int ch=getcx();int sign=1;
while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
 
while( ch >= '0' && ch <= '9' )
n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
n=n*sign;
}

int sdeg[27];
int edeg[27],start,end;
int map1[27][27];
int visited[27],c1,c2;
int flag[27];

bool euler()
{
	int f1 = 0,f2 = 0,t;
	for(int i=0;i<27;i++)
	{
		t=sdeg[i]-edeg[i];
		if(t==1)
		{
			if(f1)
				return false;
			start=i;
			f1++;
		}
		else if(t==-1)
		{
			if(f2)
				return false;
			end=i;
			f2++;
		}
		else if(t!=0)
			return false;
	}
	return true;
}

void solve(int node)
{	
	if(visited[node])
		return;
	visited[node]=1;
	c2++;
	for(int i=0;i<27;i++)
		if(map1[i][node] || map1[node][i])
			solve(i);
}

int main()
{
	int t,len;
	si(t);
	char a[1010];
	while(t--)
	{
		fill(sdeg,0);
		fill(edeg,0);
		for(int i=0;i<27;i++)
			fill(map1[i],0);
		fill(visited,0);
		fill(flag,0);
		int p,q;
		si(p);
		c1=c2=0;
		while(p--)	
		{
			scanf("%s",a);
			len = strlen(a);
			sdeg[a[0]-'a']++;
			edeg[a[len-1]-'a']++;
			map1[a[0]-'a'][a[len-1]-'a']++;
			if(!flag[a[0]-'a'])
			{
				c1++;
				flag[a[0]-'a'] = 1;
			}
			if(!flag[a[len-1]-'a'])
			{
				c1++;
				flag[a[len-1]-'a'] = 1;
			}
		}
		q=a[0]-'a';
		if(euler())
		{
			solve(q);
			//printf("c-->%c c1-->%d c2-->%d\n",q+'a',c1,c2);
			if(c1==c2)
				printf("Ordering is possible.\n");
			else
				printf("The door cannot be opened.\n");

		}
		else
			printf("The door cannot be opened.\n");
	}
	return 0;
}      
