#include<iostream>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
	int n,m;
	int k,qwe=0;
	int a[2000],maex=0,mien=0;
	cin>>n>>m;
	for(int i=0;i<m;i++)
		cin>>a[i];
	sort(a,a+m);
	int t=n;
	for(int i=0;(i<m)&&(t>0);i++)
	{
		int c=a[i];
		while(c&&(t>0))
		{
			mien+=c;
			t--;
			c--;
		}
	}
	while(n)
	{
		maex+=a[m-1];
		a[m-1]--;
		n--;
		sort(a,a+m);
	}
	cout<<maex<<" "<<mien;
	return 0;	
}