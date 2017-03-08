#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long int n,s,p,q,buy[100005],sell[100005],i;
	char ch;
	cin >> n >> s;
	memset(sell,0,sizeof(sell));
	memset(buy,0,sizeof(buy));
	while(n--)
	{
		cin >> ch >> p >> q;
		if(ch=='B')
		{
			buy[p]+=q;
		}
		else
		{
			sell[p]+=q;
		}
	}
	long long int cnt=0,j;
	for(j=0;j<=100000 && cnt<s;j++)
		if(sell[j]>0)
			cnt++;
	cnt=0;
	for(i=j;i>=0 && cnt<s;i--)
	{
		if(sell[i]>0){
			cnt++;
			cout << "S " << i <<" " << sell[i] <<endl;
		}
	}
	cnt=0;
	for(i=100000;i>=0 && cnt<s;i--)
	{
		if(buy[i]>0){
			cnt++;
			cout << "B " << i <<" " << buy[i] <<endl;
		}
	}
	return 0;
}