#include <iostream>
#include <string>
using namespace std;
int n,a[100001],s;
string t;
int main(){
	cin>>n;
	t=" ";
	for(int i=1;i<=n;i++) cin>>a[i];
	for(int i=n;i;i--) {
		if(s>0) {
			s-=a[i];
			t+="-";	
	 	} else {
	 	    s+=a[i];
	 	    t+="+";
	 	}
	}
	for(int i=n;i;i--){
	 	if(s>0) cout<<t[i];
	 	else cout<<(t[i]=='+'?'-':'+');
	}
	return 0;
}