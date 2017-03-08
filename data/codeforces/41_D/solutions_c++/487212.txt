#include<iostream>
#include<cstring>
using namespace std;

int dp[102][102][1002];
char a[102][102];
char path[102][102][1002];

int m,n,k;

void solve(int r,int c,int k)
{
//	cout<<r<<" "<<c<<" "<<k<<endl;
	if(dp[r][c][k] != -1)
		return;
	dp[r][c][k] = 1;
	static int dx[] = {-1,-1};
	static int dy[] = {-1,1};

	for(int i=0;i<2;i++){
		int X = r + dx[i];
		int Y = c + dy[i];
		if(X>=0 && X<m && Y>=0 && Y<n)
		{
			//dp[X][Y][k+a[X][Y]-48] = 1;
			if(i==0)
				path[X][Y][k+a[X][Y]-48]='L';
			else
				path[X][Y][k+a[X][Y]-48]='R';
			solve(X,Y,k+a[X][Y]-48);
		}
	}
}

string retracePath(int x,int y,int K,string p)
{
	if(x==m-1)
	{
		cout<<(y+1)<<endl;
		return p;
	}
	if(path[x][y][K] == 'L')
	{
		return retracePath(x+1,y+1,K-a[x][y]+48,"L" + p);
	}
	else
	{
		return retracePath(x+1,y-1,K-a[x][y]+48,"R" + p);
	}
}
	
int main()
{
	cin>>m>>n>>k;
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			cin>>a[i][j];
		}
	}
	memset(dp,-1,sizeof(dp));
	for(int i=0;i<n;i++){
//		dp[m-1][i][a[m-1][i] - 48] = 1;
		solve(m-1,i,a[m-1][i]- 48);
	}

	int maxm = -1;
	int indy = 0;
	for(int i=0;i<n;i++){
		for(int j=0;j<1002;j++){
			if(dp[0][i][j]!=-1  && j%(k+1)==0)
			{
				if(j>maxm)
				{
					maxm = j;
					indy = i;
				}
			}
		}
	}
	if(maxm==-1)
		cout<<"-1"<<endl;
	else
	{
		cout<<maxm<<endl;
		cout<<retracePath(0,indy,maxm,"")<<endl;
	}
	return 0;
}
