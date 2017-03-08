#include <iostream>
using namespace std;
int a[2005] = {0};
int main()
{
	int k=0,n,i,j,max=0;
	cin>>n;
	for(i=1;i<=n;i++)	cin>>a[i];
	for(i=1;i<=n;i++)
	{
		for(j=i,k=1;j!=-1;k++,j=a[j])
			if(k>max)	max=k;
	}
	cout<<max<<endl;
	return 0;
}
