#include <iostream>
#include <algorithm>
using namespace std;
int n,k,p,x,y,scr[1000];
int main()
{
	int i,cnt,c2=0;
	cin>>n>>k>>p>>x>>y;
	for (i=1;i<=k;i++)
	{
		cin>>scr[i];
		c2+=scr[i];
	}
	sort(scr+1,scr+k+1);
	for (cnt=1;scr[cnt]<y&&cnt<=k;cnt++);
	cnt--;
	if (cnt>(n-1)/2)
	{
		cout<<-1;
		return 0;
	}
	cnt=(n-1)/2-cnt;
	if (cnt+(n-k-cnt)*y>x-c2||c2>=x)
	{
		cout<<-1;
		return 0;
	}
	for (i=1;i<=n-k;i++)
	{
		if (i<=cnt)
			cout<<1<<" ";
		else
			cout<<y<<" ";
	}
	return 0;
}
