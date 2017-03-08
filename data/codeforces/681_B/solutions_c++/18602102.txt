#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n;
	cin>>n;
	for(int i=0;i<=n;i+=1234567)
	{
		for(int j=0;j+i<=n;j+=123456)
		{
			if((n-i-j)%1234==0)
			{
				cout<<"YES\n";
				return 0;
			}
		}
	}
	cout<<"NO\n";
	return 0;
}