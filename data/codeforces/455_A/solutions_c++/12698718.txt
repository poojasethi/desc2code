#include<iostream>
#include<algorithm>
using namespace std;
long long int a[100006]={0},dp[100006]={0};
int main(){
	int n,i,j,k;
	cin>>n;
	while(n--){
		cin>>k;
		a[k]++;
	}
	dp[1]=a[1];
	for(i=2;i<=100002;i++)dp[i]=max(dp[i-1],dp[i-2]+a[i]*i);
	cout<<dp[100002]<<endl;	
}