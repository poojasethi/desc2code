#include<iostream>
int L[105];
using namespace std;
int main()
{
	int n;
	cin>>n;
	int a,b;
	cin>>a>>b;
	int ta,tb;
	for(int i=0;i<n-1;i++)
	{
		cin>>ta>>tb;
		for(int i=ta;i<tb;i++)
			L[i]++;
	}
	int cnt=0;
	for(int i=a;i<b;i++)
	{
		if(!L[i])
			cnt++;
	}
	cout<<cnt<<endl;
}
