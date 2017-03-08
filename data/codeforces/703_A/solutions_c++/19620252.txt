#include <iostream>
using namespace std;
main()
{
	int n,a=0,b=0,x,y;
	cin>>n;
	for (int i=1;i<=n;i++)
	{
		cin>>x>>y;
		if (x>y) a++;
		else if (x<y) b++;
	}
	if (a>b) cout<<"Mishka"<<endl;
	else if (a<b) cout<<"Chris"<<endl;
	else cout<<"Friendship is magic!^^"<<endl;
}
