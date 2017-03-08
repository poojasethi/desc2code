#include <iostream>

using namespace std;

int main(){
	int n;
	cin>>n;
	bool flag=false;
	for(int i=0;i<4;i++){
		int a,b,c,d;
		cin>>a>>b>>c>>d;
		int A=min(a,b);
		int B=min(c,d);
		if(A+B<=n&&!flag){
			cout<<i+1<<" "<<A<<" "<<n-A<<endl;
			flag=true;
		}
	}
	if(!flag)
		cout<<"-1"<<endl;
}
