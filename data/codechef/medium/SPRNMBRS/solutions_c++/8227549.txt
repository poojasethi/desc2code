#include<bits/stdc++.h>
#define ull unsigned long long int
using namespace std;
#define MAXN 1e18
vector<ull>V;
int main()
{
	int t;
	ull i,j,l,r,ans,c,a,b;
	ull  num,fnum;
	scanf("%d",&t);
	V.push_back(1);
	num=2;
	for(j=1;j<64;j++)
	{
		fnum=num;
		for(i=0;i<40;i++)
		{
			V.push_back(fnum);
			//cout<<fnum<<" ";
			fnum=fnum*3;
			if(fnum>MAXN)
				break;
		}
		num=num*2;
		if(num>MAXN)
			break;
	}
	sort(V.begin(),V.end());
	V.erase( unique( V.begin(), V.end() ), V.end() );
	vector<ull>::iterator it;
//	cout<<V[V.size()-1]<<endl;
//	for(i=0;i<100;i++)
//	cout<<V[i]<<" ";
//	cout<<endl;
	while(t>0)
	{
		t--;
		scanf("%llu %llu",&l,&r);
		it=lower_bound(V.begin(),V.end(),r);
		b=lower_bound(V.begin(),V.end(),l)-V.begin();
		if(it!=V.end()){
			if(*it>r)
				a=it-V.begin()-1;
				else
				a=it-V.begin();
		}
		else
		{
			a=V.size()-1;
		}
		c=a-b+1;
		printf("%llu\n",c);
	}
}
