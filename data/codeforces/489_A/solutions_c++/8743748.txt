#include <iostream>
using namespace std;

int a[3000];
int sw[3000];

int main()
{
	int n;
	cin >> n;
	for(int i=0;i<n;i++)
		cin >> a[i];
	
	for(int i=0;i<n;i++)
	{
		int m=i;
		for(int j=i+1;j<n;j++)
			if(a[m]>a[j])
				m=j;
		swap(a[i], a[m]);
		sw[i] = m;
	}
	
	cout << n << endl;
	for(int i=0;i<n;i++)
		cout << i << ' ' << sw[i] << endl;
	return 0;
}

