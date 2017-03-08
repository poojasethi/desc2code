#include <cstdio>
#include <iostream>
using namespace std;
int a[400001];
int main(){
	long long n,ans,len;
	while(cin>>n){
		int min=1000000000;
		for(int i=0;i<n;i++){
			scanf("%d",&a[i]);
			a[i+n]=a[i];
			min=a[i]<min?a[i]:min;
		}
		ans=n*min;
		len=0;
		for(int i=0,j;i<2*n;i++){
			if(a[i]>min){
				j=i;
				while(a[j]>min) j++;
				len=j-i>len?j-i:len;
				i=j-1;
			}
		}
		cout<<ans+len<<endl;
	}
}