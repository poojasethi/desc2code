/* bhupkas */

#include "iostream"
#include "stdio.h"

using namespace std;

#define FOR(i,a,b)		for(i=a;i<b;i++)
#define MAX			205
#define INF			1000000000

int A[MAX+5][MAX+5];
int n,m,k,c;
bool B[MAX+5][MAX+5];
bool visited[MAX+5];
int N[MAX+5];

bool done(int num)
	{
		int i; 
		if(visited[num])	return false;
		visited[num]=true;
		FOR(i,0,2*m)
			{
				if(B[num][i])
					{
						if(N[i]==-1 || done(N[i]))
							{
								N[i]=num;
								return true;
							}
					}
			}
		return false;
	}

int fun(int num)
	{
		int i,j,foo;
		FOR(i,0,n)	FOR(j,0,2*m)	B[i][j]=false;
		FOR(i,0,n)
			{
				FOR(j,0,m)
					{
						if(A[i][j]<=num)	B[i][j]=true;
						if(A[i][j]+c<=num)	B[i][j+m]=true;
					}			
			}
		FOR(i,0,2*m)	N[i]=-1;
		foo=0;
		FOR(i,0,n)
			{
				FOR(j,0,n)	visited[j]=false;
				if(done(i))	foo++;	
			}
		return foo;
	}

int main()
	{
		int i,j,t,low,high,mid,ans;
		cin>>t;
		while(t--)
			{
				cin>>n>>m>>k>>c;
				FOR(i,0,n)
					FOR(j,0,m)	
						cin>>A[i][j];
				ans=INF;
				low=0;
				high=ans;
				while(low<=high)
					{
						mid=(low+high)/2;
						if(fun(mid)>=k)
							high=mid-1,ans=mid;
						else
							low=mid+1;
					}
					cout<<ans<<endl;
			}
		return  0;
	}
