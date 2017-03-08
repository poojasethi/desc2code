#include <iostream>
#include <vector>

using namespace std;

#define ll long long int

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		ll gold,x=0,y=100000;
		cin>>gold;
		while(y-x>1)
		{
			ll mid = (x+y)/2;
			if((mid*(mid+1))/2<=gold)x=mid;
			else y=mid;
		}
		cout<<x<<endl;
	}
}