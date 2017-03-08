#include<iostream>
int fa[101],a[101][101],b[101]={0},n1,m1;
using namespace std;

int fffa(int n)
{
	return fa[n]==n? fa[n]:fa[n]=fffa(fa[n]);
}

int main()
{
	int i,j,num=0,t,flag=0,lang;
	cin>>n1>>m1;
	for(i=1;i<=n1;i++)
	{
		fa[i]=i;
		cin>>t;
		for(j=1;j<=t;j++)
		{
			flag=1;
			cin>>lang;
			if(b[lang]==0)b[lang]=i;
			else fa[fffa(b[lang])]=i;
		}
	}
	for(i=1;i<=n1;i++)
	{
		if(fa[i]==i)
		{
			num++;
		}
	}
	cout<<num-flag;
	return 0;
}