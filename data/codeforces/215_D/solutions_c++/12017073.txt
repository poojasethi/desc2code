#include<bits/stdc++.h>
using namespace std;
long long sum=0;

int main()
{
	int i,n,m,num;
	long long sum=0,tmp1,tmp2,t,T,x,cost;
	scanf("%d%d",&n,&m);
	for(i=1;i<=n;i++){
		cin>>t>>T>>x>>cost;
		tmp1=tmp2=0x7ffffffffff;
		if(m+t<=T) tmp1=cost;
		else tmp1=cost+m*x;
		if(T>t){
			num=m/(T-t);
			if(m%(T-t)) num++;
			tmp2=num*cost;
		}
		sum+=min(tmp1,tmp2);
	}
	cout<<sum;
 return 0;
}
