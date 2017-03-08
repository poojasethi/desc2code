#include <iostream>
using namespace std;
int main(){
	int n;
	cin>>n;
	int arr[10001]={0};
	for(int i=0;i<n;i++)
	{
		int x;cin>>x;
		arr[x]++;
	}
	int ans=0;
	for(int i=1;i<=998;i++)
	{
		if(arr[i] && arr[i+1] && arr[i+2])
		{
			ans=1;
			break;
		}
	}
	if(ans)
		cout<<"YES\n";
	else
		cout<<"NO\n";
}