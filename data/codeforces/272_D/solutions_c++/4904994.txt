#include <cstdio>
#include <iostream>
#include <map>
#define N 100010

typedef long long LL;
using namespace std;

int a[N],b[N];
map<int,int> mp;
map<int,int>::iterator it;

int main() {
	int n,m,two;
	scanf("%d",&n);
	for(int i=0; i<n; i++) {
		scanf("%d",&a[i]);
		mp[a[i]]++;
	}
	for(int i=0; i<n; i++) { 
		scanf("%d",&b[i]);
		mp[b[i]]++;
	}
	two=0;
	for(int i=0; i<n; i++)
		if(a[i]==b[i])
			two++;
	scanf("%d",&m);
	LL ret=1;
	for(it=mp.begin(); it!=mp.end(); it++) {
		for(int i=1; i<=it->second; i++) {
			int x=i;
			for(; two>0&&(!(x&1));)
				x>>=1,two--;
			ret=ret*x%m;
		}
	}
	cout<<ret<<endl;
	return 0;
}
