/* bhupkas */

#include "iostream"

using namespace std;

#define FOR(i,a,b)	for(i=a;i<b;i++)

int a[100001]={0};
int b[100001];

int main()
	{
		int l=0,r,ans=0,n,i,k;
		cin>>n>>k;
		FOR(i,0,n)
			{
				cin>>b[i];
				if(!a[b[i]])	ans++;
				a[b[i]]++;
				if(ans==k)
					{
					  r=i;
					  break;
					}
			}
		if(ans==k)
		{
			while(l<r&&a[b[l]]>1)
				{
					a[b[l]]--;l++;
				}
			cout<<l+1<<" "<<r+1<<endl;
		}
		else cout<<"-1 -1"<<endl;
		return 0;
	}
