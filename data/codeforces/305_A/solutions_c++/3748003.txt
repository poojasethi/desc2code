#include <iostream>
using namespace std;

int main()
{
	int n;
	int a[1000],b[1000];
	cin>>n;
	int f2=0,f1=0,flag=0,te=0;
	int p=0;
	for(int i=0;i<n;i++){
		cin>>a[i];
		if(a[i]==100 || a[i]==0){
			b[p]=a[i];
			p++;
		}
		else if(a[i]%10 == 0){
			te=a[i];
		}
		else if(a[i]<10){
			f1=a[i];
		}
		else{
			f2=a[i];
		}
		
	}
	if(te && f1){
		b[p]=te;
		b[p+1]=f1;
		p+=2;
	}
	else if(te){
		b[p]=te;p++;
	}
	else if(f1){
		b[p]=f1;p++;
	}
	else if(f2 && !te && !f1){
		b[p]=f2;
		p++;
	}
	cout<<p<<endl;
	for(int i=0;i<p;i++){
		cout<<b[i]<<" ";
	}
	return 0;
}
