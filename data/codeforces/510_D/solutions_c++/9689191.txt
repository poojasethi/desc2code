#include<bits/stdc++.h>
using namespace std;

int gcd(int a,int b){
	return a?gcd(b%a,a):b;
}

int main(){
	int n;
	cin>>n;
	int a[310],c[310];
	for(int i=0;i<n;i++)
		cin>>a[i];
	for(int i=0;i<n;i++)
		cin>>c[i];
	map<int,int> mp;
	map<int,int>::iterator it;
	for(int i=0;i<n;i++){
		int &x=mp[a[i]];
		if(x==0)
			x=c[i];
		else
			x=min(x,c[i]);
		for(it=mp.begin();it!=mp.end();it++){
			int &y=mp[gcd(a[i],it->first)];
			if(y==0)
				y=it->second+c[i];
			else
				y=min(y,it->second+c[i]);
		}
	}
	if(mp[1]==0)
		puts("-1");
	else
		printf("%d\n",mp[1]);
}
