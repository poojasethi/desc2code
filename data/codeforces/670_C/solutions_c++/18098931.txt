
#include<bits/stdc++.h>

using namespace std;

typedef long long int 	LL;
map <LL, int> l;
LL best=0;int bs=0;
LL k,m,a[400002],b[400005],n,s;
int main(){
	cin >> n;
	for(int i=0;i<n;i++){
		scanf("%lld",&k);
		l[k]++;
	}
	cin >> m;
	for(int i=0;i<m;i++){
		scanf("%lld",&s);
		a[i]=s;
	}	

	for(int i=0;i<m;i++){
		scanf("%lld",&s);
		b[i]=s;
		if(l[a[i]]>l[a[best]]){
			best=i;
		}
		else if(l[a[i]]==l[a[best]] && l[b[i]]>l[b[best]]){
			best = i;
		}
	}
	
	cout << best+1 << endl;
	return 0;
}