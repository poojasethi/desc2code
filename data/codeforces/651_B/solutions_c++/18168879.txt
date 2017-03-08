#include <iostream>
#include <algorithm>
using namespace std;
int n,cnt[1001];
int main()
{
	cin>>n;
	for(int i=0; i<n; i++)
	{
		int tmp;
		cin>>tmp;
		cnt[tmp]++;
	}
	cout<<(n-*max_element(cnt,cnt+1001))<<endl;
}

