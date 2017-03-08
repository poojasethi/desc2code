#include <iostream>
#include <math.h>

using namespace std;

int main(){
	int n;
	long long a,b;
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>a;
		b=sqrt(a);
		int j;
		for(j=2;j*j<=b;j++) 
			if(b%j==0) 
				break;
		if(j*j>b&&b*b==a&&a>1) 
			cout<<"YES\n";
		else 
			cout<<"NO\n";
	}
}
