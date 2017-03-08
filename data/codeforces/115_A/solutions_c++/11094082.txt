#include<bits/stdc++.h>
using namespace std;
int a[2005];
int main()
{
	int k=0,n,i,j,ma=0;
	cin>>n;
	for(i=1;i<=n;i++) cin>>a[i];
	for(i=1;i<=n;i++)
		for(j=i,k=1;j!=-1;k++,j=a[j])
            ma=max(k,ma);
	cout<<ma<<endl;
	return 0;
}
