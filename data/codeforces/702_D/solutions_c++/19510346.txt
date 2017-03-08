#include<bits/stdc++.h>
#define LL long long int
using namespace std;
int main(){
	LL d,k,a,b,t;
	cin>>d>>k>>a>>b>>t;
	if(d<=k)
		cout<<d*a;
	else if((t+k*a)>(k*b))
		cout<<k*a + (d-k)*b;
	else{
		LL cnt = d/k;
		cout<<k*cnt*a+(cnt-1)*t+min(t+(d%k)*a,(d%k)*b);
		
	}
	return 0;	
}
