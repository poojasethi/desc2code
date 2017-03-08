#include <iostream>
#include <algorithm>
using namespace std;
struct  str
{
	int type,cost,q;
};
bool structsorter(str const& lhs,str const& rhs)
{
	if(lhs.q!=rhs.q)return lhs.q<rhs.q;
	else if(lhs.cost!=rhs.cost)return lhs.cost<rhs.cost;
	else return lhs.type<rhs.type;
};


int main()
{
	int n,t;
	cin>>n>>t;
	str a[n];
	for(int i=0;i<n;i++)
	{
		cin>>a[i].type>>a[i].cost>>a[i].q;
	}
	sort(a,a+n,structsorter);
	int sol=0;
	int tcost=0;
	int tempcost[7]={0};
	int b[7];
	for(int i=0;i<n;i++)
	{	for(int k=0;k<7;k++)b[k]=0;
		for(int k=0;k<7;k++)tempcost[k]=0;
		tcost=0;
		if(a[i].type>6 || a[i].type<1)continue;
		else{
			b[a[i].type]=1;tcost+=a[i].cost;
			for(int j=i+1;j<n;j++)
			{	if(a[j].type>6 || a[j].type<1)continue;
				else if(b[a[j].type]==0){b[a[j].type]=1;tcost+=a[j].cost;tempcost[a[j].type]=a[j].cost;}
				else if(b[a[j].type]==1)
				{
					if(a[j].cost<tempcost[a[j].type]){tcost-=tempcost[a[j].type];tcost+=a[j].cost;tempcost[a[j].type]=a[j].cost;}
				}
			}
			int flag=0;
			for(int k=1;k<=6;k++)
				{if(b[k]==0)flag=1;}
			if(flag==0 && tcost<=t)sol=a[i].q;
			//cout<<"sol "<<sol<<endl;
		}
	}
	cout<<sol<<endl;


}

