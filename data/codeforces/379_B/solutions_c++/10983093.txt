#include <iostream>
using namespace std;
int main()
{
	int n,i,j,t;
	cin>>n;
	for (i=1;i<=n;i++)
	{
		cin>>t;
		for (j=1;j<=t;j++)
			cout<<(i<n?"PRL":"PLR");
		cout<<(i<n?"R":"");
	}
	return 0;
}
