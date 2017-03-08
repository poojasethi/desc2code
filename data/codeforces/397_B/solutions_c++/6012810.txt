#include<iostream>
#include<cmath>
#define ll long long
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		ll n,l,r;
		cin>>n>>l>>r;
		int temp;
		temp=floor(n/l+0.5);
		if(temp*r>=n)
			cout<<"Yes"<<endl;
		else
			cout<<"No"<<endl;
	}
	return 0;
}
