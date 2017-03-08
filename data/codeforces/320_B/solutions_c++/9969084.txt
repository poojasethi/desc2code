#include <iostream>
#include <algorithm>
#include <memory.h>
using namespace std;
pair<int,int> a[101];
bool vst[101];
int sm;
void src(int k)
{
	int i;
	vst[k]=true;
	for (i=1;i<=sm;i++)
		if ((a[k].first>a[i].first&&a[k].first<a[i].second||a[k].second>a[i].first&&a[k].second<a[i].second)&&!vst[i])
			src(i);
}
int main()
{
	int n,flg,x,y,i,j;
	cin>>n;
	for (i=1;i<=n;i++)
	{
		cin>>flg>>x>>y;
		if (flg==1)
		{
			sm++;
			a[sm].first=x;
			a[sm].second=y;
		}
		else
		{
			for (j=1;j<=sm;j++)
				vst[j]=false;
			src(x);
			if (vst[y])
				cout<<"YES";
			else
				cout<<"NO";
			cout<<endl;
		}
	}
	return 0;
}
