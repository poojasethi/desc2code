#include <iostream>
#include <cstring>
#include <cmath>
#include <fstream>
#define cin fin
#define cout fout

using namespace std;

int main ()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int m,k;
	cin >> m>> k;
	bool mm[110]={};
	int p;
	for (int i=0;i<k;i++)
	{
		cin >> p;
		mm[p]=1;
	}
	int n;
	cin >> n;
	int mx[101]={},mn[101]={};
	for (int i=0;i<n;i++)
	{
		string s;
		cin >> s;
		int ac;
		cin >> ac;
		int p;
		int minr=0,Max=0,maxr=0;
		for (int i=0;i<ac;i++)
		{
			cin >> p;
			if (p==0) 
				Max++;
			if (mm[p]) 
				minr++;
		}
		maxr = min(k, Max+minr);		
		minr = max(minr, k+ac-m);

		mx[i]=maxr;
		mn[i]=minr;
	}	
	for (int i=0;i<n;i++)
	{
		bool ok0=1,ok1=0;
		for (int j=0;j<n;j++)
			if (i!=j)
			{
				if (mn[i]<mx[j])
					ok0=0;
				if (mx[i]<mn[j])
					ok1=1; 	
			}
		if (ok0) 
			cout << 0 << endl;
		else if (ok1) 
			cout << 1 << endl;
		else
			 cout << 2 << endl;
	}
	fout.close();			
	return 0;
}