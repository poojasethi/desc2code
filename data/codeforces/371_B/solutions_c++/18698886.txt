#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
ios_base::sync_with_stdio(0);
	int a,b,c=0;
	cin>>a>>b;
	for(int i = 2; i < 6; ++i)
	{
		while(a%i == 0 && b%i == 0)a/=i,b/=i;
		while(a%i == 0)++c,a/=i;
		while(b%i == 0)++c,b/=i;
	}
	if(a!=b)c=-1;
	cout<<c;
	return 0;
}
