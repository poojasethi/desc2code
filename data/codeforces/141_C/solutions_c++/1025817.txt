#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int n,h[3010];
struct Persoana{char nume[15];int nr;};
Persoana P[3010];
vector <int> poz;

inline bool Sortare(Persoana A,Persoana B)
{
	return A.nr<B.nr;
}

int main()
{
	int i;
	cin>>n;
	for(i=1;i<=n;i++)
		cin>>P[i].nume>>P[i].nr;
	
	sort(P+1,P+n+1,Sortare);
	poz.push_back(0);
	for(i=1;i<=n;i++)
	{
		if(P[i].nr>=i)
		{
			cout<<"-1\n";
			return 0;
		}
		poz.insert(poz.begin()+(P[i].nr+1),i);
	}
	for(i=1;i<=n;i++)
		h[poz[i]]=n-i+1;
	for(i=1;i<=n;i++)
		cout<<P[i].nume<<' '<<h[i]<<"\n";
	return 0;
}
