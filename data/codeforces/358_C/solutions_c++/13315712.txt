#include <bits/stdc++.h>
using namespace std ;
typedef pair <long long int, long long int> ii;
const long long int Maxn = 100005;
const string ins[4] = {"pushBack", "pushStack", "pushQueue", "pushFront"};
const string nam[3] = {"popStack", "popQueue", "popFront"};
long long int n;
long long int a[Maxn];
priority_queue<ii> Q;
long long int taken[Maxn];
long long int cnt[3];
int main()
{
	cin >> n ;
	for(long long int i=0;i<n;i++) 
	{
		cin >> a[i] ;
		if(a[i])
		{ 
			Q.push(ii(a[i],i));
		}
		else 
		{
			long long int len = 0;
			while(!Q.empty() && len<3) 
			{
				taken[Q.top().second] = len + 1; 
				Q.pop();
				len++;
			}
			taken[i] = len;
			while(!Q.empty()) 
				Q.pop();
		}
	}
	for(long long int i = 0; i < n; i++)
	{
		if(a[i])
		{ 
			cout << ins[taken[i]].c_str() << "\n" ;
		}
		else 
		{
			cout << taken[i] ;
			for(long long int j = 0; j < taken[i]; j++)
				cout << " " << nam[j].c_str() ;
			cout << "\n" ;
		}
	}
	return 0;
}