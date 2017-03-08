# include <iostream>
# include <vector>
# include <algorithm>

# define MAXN 100009

using namespace std;

vector <int> D[MAXN];

int n, P[MAXN][5], t;

int main()
{
	cin>>n;
	
	for(int h=0; h<n; h++)
	{int a;
		cin>>a;
		D[a].push_back(h);
	}
	
	for(int h=0; h<MAXN-5; h++)
		if((int)D[h].size() != 0)
		{
			int ans = 0, p = 1;
			
			for(int j=1; j<(int)D[h].size(); j++)
			{
				if(ans  &&  ans != D[h][j]-D[h][j-1])	p = 0;
				ans = D[h][j]-D[h][j-1];
			}
			
			if(p)	P[t][0] = h, P[t++][1] = ans;
		}
	
	cout<<t<<"\n";
	
	for(int h=0; h<t; h++)
		cout<<P[h][0]<<" "<<P[h][1]<<"\n";
}
