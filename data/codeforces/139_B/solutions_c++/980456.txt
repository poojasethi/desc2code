#include<iostream>
using namespace std;
int n,m,P[505],L[505],l[505],h[505],x[505],y[505],c[505],sol,solt;
int main()
{
	int i,j,aux,lg;
	cin>>n;
	for(i=1;i<=n;i++)
	{
		cin>>L[i]>>l[i]>>h[i];
		P[i]=2*(L[i]*h[i]+l[i]*h[i]);
	}
	cin>>m;
	for(i=1;i<=m;i++)
	{
		cin>>x[i]>>y[i]>>c[i];
	}
	for(i=1;i<=n;i++)
	{
		sol=2000000000;
		lg=2*(L[i]+l[i]);
		for(j=1;j<=m;j++)
		{
			aux=x[j]/h[i];
			aux*=y[j];
			if(aux!=0)
			{
				if(lg%aux==0)
					sol=min(sol,(lg/aux)*c[j]);
				else
					sol=min(sol,((lg/aux)+1)*c[j]);
			}
		}
		solt+=sol;
	}
	cout<<solt<<"\n";
	return 0;
}
