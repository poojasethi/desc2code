#include<bits/stdc++.h>
using namespace std;
int p[109];
int main()
{
	int n,m,k,i,j,g,x;
	cin>>n>>m>>k;
	for(i=1;i<=k;i++)
	{
		cin>>x;
		p[x]=i;
	}
	int tot=0;
	for(i=0;i<n;i++){
		for(j=0;j<m;j++){
			cin>>x;
			tot+=p[x];
			for(g=1;g<=k;g++)
				if(p[g]<p[x])
					p[g]++;
			p[x]=1;
		}
	}
	cout<<tot;
	return 0;
}
