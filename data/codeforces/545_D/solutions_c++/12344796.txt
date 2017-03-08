#include<stdio.h>
#include<algorithm>
using namespace std;
int a[100009];
int main(){
	int n,i;
	scanf("%d",&n);
	for(i=0;i<n;i++)scanf("%d",&a[i]);
	sort(a,a+n);
	int c=0;
	long long int s=0;
	for(i=0;i<n;i++){
		if(a[i]>=s){
			s+=a[i];
			c++;
		}
	}
printf("%d\n",c);



}