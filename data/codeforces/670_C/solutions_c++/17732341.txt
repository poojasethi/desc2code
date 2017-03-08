#include <iostream>
#include <map>
#define FOR(i,a,b) for(int i=a; i<b; i++)
#define dbug(x) #x<<": "<<x<<' '
using namespace std;
int n,m,maxb,maxc,ind;
int b[200001],c[200001];
map<int,int> speakers;
int main()
{
	cin>>n;
	FOR(i,0,n)
	{
		int tmp;
		cin>>tmp;
		speakers[tmp]++;
	}
	cin>>m;
	FOR(i,0,m)
		cin>>b[i];
	FOR(i,0,m)
		cin>>c[i];
	FOR(i,0,m)
	{
		if(speakers[b[i]]>maxb || ((speakers[b[i]]==maxb) && (speakers[c[i]]>maxc) ) )
		{
			maxb = speakers[b[i]];
			maxc = speakers[c[i]];
			ind = i;
		}
	}
	cout<<ind+1<<endl;
}
