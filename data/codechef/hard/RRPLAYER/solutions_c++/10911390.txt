#include<bits/stdc++.h>

using namespace std;


int main()
{
	vector<double> temp;
	temp.resize(4000);
	for(int i=1;i<4000;i++)
	{
		temp[i]=1.0/double(i);
		temp[i]+=temp[i-1];
	}
	int t;
	cin>>t;
	int n;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		cout<<fixed<<setprecision(1)<<temp[n]*double(n)<<endl;
	}
}