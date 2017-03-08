#include<iostream>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<utility>
#include<iomanip>
#include<queue>

using namespace std;

#define INF (1<<29)
#define SET(a) memset(a,-1,sizeof(a))
#define ALL(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define FILL(a,v) memset(a,v,sizeof(a))
#define PB push_back
#define FOR(i,n) for(int i = 0;i<n;i++)
#define PI acos(-1.0)
#define EPS 1e-9
#define MP(a,b) make_pair(a,b)
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define READ freopen("input.txt", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)
#define LL long long
#define MX 1003
#define MOD 100000000

#define p(x) printf("%d",x)
#define inp(x) scanf("%d",&x)
#define inpd(x) scanf("%lf",&x)
#define inpll(x) scanf("%lld",&x)
#define getcx getchar_unlocked
/*inline void inp( int &n )
 {
 n=0;
 int ch=getcx();int sign=1;
 while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
 
 while(  ch >= '0' && ch <= '9' )
 n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
 n=n*sign;
 }*/


using namespace std;

bool check[MX];
int p[MX],n,m,num;
vector<int> a[MX];
vector<int> cycle;
int sol[3][4]={{1,7,8,11},{4,5,6,10},{2,3,9,12}};

void assigne()
{
    int l=cycle.size();
    //cout<<"\nl = "<<l;
    int lmt = num+l*m;
    int i=l-1,cnt=0;
    if(l==3 && m==4)
    {
        for(i=0;i<4;i++)
            a[cycle[0]].PB(num+sol[0][i]-1);
        for(i=0;i<4;i++)
            a[cycle[1]].PB(num+sol[1][i]-1);
        for(i=0;i<4;i++)
            a[cycle[2]].PB(num+sol[2][i]-1);
        num+=12;
        return ;
    }
    
    while(num!=lmt)
    {
        a[cycle[i]].PB(num);
        num++;
        cnt++;
        if(cnt==l)
        {
            cnt=0;
            continue;
        }
        else
            i--;
        
        if(i<0)
            i=l-1;
    }
}

int main()
{
    int t=0;
    inp(t);
    while(t--)
    {
        CLR(a);
        inp(n);
        inp(m);
        for(int i=0;i<n;i++)
            inp(p[i]);
        CLR(check);
        
        num=1;
        bool b=0;
        int no,l;
        
        for(int i =0;i<n;i++)
		{
            cycle.clear();
			if(!check[i])
			{
				check[i]=1;
                cycle.PB(i);
				no = p[i];
                while(1)
				{
					if(no==i)
					{
                        if(cycle.size()<3)
                        {
                            cout<<"No Solution\n";
                            b=1;
                            break;
                        }
                        assigne();
						break;
					}
					else
					{
						check[no]=1;
                        cycle.PB(no);
						no = p[no];
					}
				}
			}
            if(b)
            break;
		}
        if(b)
        continue;
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<a[i].size();j++)
            {
                cout<<a[i][j]<<" ";
            }
            cout<<endl;
        }
        
    }
    return 0;
}
