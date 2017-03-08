//279B
#include<iostream>
using namespace std;

int main()
{
	int t,n;
	int arr[100010];
	cin>>t>>n;
	int k=t;
	int i=0;
	int j=0;
	int sum=0;
	while(t--)
	{
	       cin>>arr[j];
		sum=sum+arr[j];
		j++;
		if(sum>n)
		{
			sum=sum-arr[i];
			i++;
		}
	}
	cout<<(k-i);
}
