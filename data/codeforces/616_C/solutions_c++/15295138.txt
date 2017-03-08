#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

char A[1002][1002];
int B[1002][1002];
int c;
vector<int> D;

void f(int a1, int a2)
{
	if(A[a1][a2] != '.')return;
	A[a1][a2] = ' ';
	B[a1][a2] = D.size();
	++c;
	f(a1-1,a2);
	f(a1+1,a2);
	f(a1,a2-1);
	f(a1,a2+1);
}

int main()
{
ios_base::sync_with_stdio(0);
	int n,m;
	cin>>n>>m;
	D.push_back(0);
	for(int i = 1; i <= n; ++i)
	{
		for(int j = 1; j <= m; ++j)
		{
			cin>>A[i][j];
		}
	}
	for(int i = 1; i <= n; ++i)
	{
		for(int j = 1; j <= m; ++j)
		{
			if(!B[i][j] && A[i][j] == '.')
			{
				c = 0;
				f(i,j);
				D.push_back(c);
			}
		}
	}
	for(int i = 1; i <= n; ++i)
	{
		for(int j = 1; j <= m; ++j)
		{
			if(A[i][j] == '*')
			{
				int r = 1;
				set<int> s;
				s.insert(B[i-1][j]);
				s.insert(B[i+1][j]);
				s.insert(B[i][j-1]);
				s.insert(B[i][j+1]);
				for(set<int>::iterator l = s.begin(); l != s.end(); ++l) r+=D[*l];
				cout<<r%10;
			}
			else cout<<'.';
		}
		cout<<'\n';
	}
	return 0;
}
