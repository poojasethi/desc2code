#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

int A[1111][1111];
bool fg[1111];
int main() {
	int n,m,a=0,b=0,x;
	cin>>n>>m;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j <m ; ++j)
		{
			cin>>x;
			if(x==11)
				a++;
			else if(x==1 || x==10)
				b++;
		}
	}
	// cout<<"a "<<a<<" b "<<b<<endl;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			if(a>0){
				A[i][j]=11;
				a--;	
				continue;
			}	
		}	
	}

	for (int i = 0; i < n; ++i)
	{
		for (int j = m-1; j >=0; --j)
		{
			if(A[i][j]>0)
				continue;
			if(b>0 && fg[j]){
				A[i][j]=1;
				b--;
				fg[j]=0;	
				continue;
			}	
			else if(b>0 && !fg[j]){

				A[i][j]=10;
				 b--;
				 fg[j]=1;
				 continue;
			}
		}	
	}

	for (int i = 0; i < n ; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			if(A[i][j]==11)
				cout<<"11 ";
			else if(A[i][j]==10)
				cout<<"10 ";
			else if(A[i][j]==1)
				cout<<"01 ";
			else
				cout<<"00 ";
		}
		cout<<endl;
	}		
	return 0;
}