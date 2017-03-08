#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <limits.h>
using namespace std;
typedef long long LL;
int main(){
	LL n,s=LLONG_MAX,l=-1;
	cin>>n;
	for(LL a=1;a*a<=n;a++)
		if(n%a==0)
			for(LL b=1;b*b<=n/a;b++)
				if((n/a)%b==0){
					LL c=(n/a)/b;
					LL A=a+1,B=b+2,C=c+2;
					s=min(s,A*B*C-n);
					l=max(l,A*B*C-n);
					A=a+2,B=b+1,C=c+2;
					s=min(s,A*B*C-n);
					l=max(l,A*B*C-n);
					A=a+2,B=b+2,C=c+1;
					s=min(s,A*B*C-n);
					l=max(l,A*B*C-n);
				}
	cout<<s<<" "<<l<<endl;
	return 0;
}

