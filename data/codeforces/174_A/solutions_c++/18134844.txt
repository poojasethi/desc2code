#include<iostream>

#define FOR(i,a,b) for(int i=a;i<b;i++)

using namespace std;

int main()
{
	int n,b;
	cin>>n>>b;
	double a[100];
	double sum = b;
	FOR(i,0,n)
	{
		cin>>a[i];
		sum+=a[i];
	}
	sum/=n;
	bool flag = true;
	FOR(i,0,n)
	{
		a[i] = sum - a[i];
		if(a[i]<0)
			flag = false;
	}
	if(!flag)
		cout<<-1<<endl;
	else
	{
		cout.precision(9);
		FOR(i,0,n)
			cout<<a[i]<<endl;
	}
}
