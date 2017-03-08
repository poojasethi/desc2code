#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int test=0;test<t;test++)
	{
		int n;
		cin>>n;
		vector<unsigned int> vec;
		vec.resize(1001);
		for(int i=0;i<=1000;i++)vec[i]=0;
		int count=0,temp,var=0;
		for(int i=0;i<n;i++)
		{
			cin>>temp;
			vec[temp]++;
			var=var^temp;
		}
		for(int i=1;i<=1000;i++)
		{
			if(vec[i]%2==1)count++;
			
		}
		if(var==0)cout<<"First"<<endl;
		else if(count%2==1)cout<<"Second"<<endl;
		else cout<<"First"<<endl;
	}
}