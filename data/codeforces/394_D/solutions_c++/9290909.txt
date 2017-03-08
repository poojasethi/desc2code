#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;
std::vector<int> v;
int main() {
	int n,x;
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		cin>>x;
		v.push_back(x);
	}
	sort(v.begin(), v.end());
	int st=0,minim=1e9,maxim,d;
	for (int diff = 0; diff <= 20000; ++diff)
	{
		maxim=-1;
		int s=v[0];
		int l=0,r=0;
		for (int i = 1; i < n; ++i)
		{
			l=min(l,s+i*diff-v[i]);
			r=max(r,s+i*diff-v[i]);
		}
		int dd=(r-l)/2;
		dd=max(r-l-dd,dd);
		if(dd<minim){
			minim=dd;
			st=s+(dd-r);
			d=diff;
		}
	}
	cout<<minim<<endl<<st<<" "<<d<<endl;
	return 0;
}