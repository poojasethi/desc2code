#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,i,j,a[3004];
	cin >> n;
	for(i=0;i<n;i++)
		cin >> a[i];
	cout << n << endl;
	for(i=0;i<n;i++)
	{
        int mi=i;
        for(j=i;j<n;j++)
        	if(a[mi]>a[j])
        		mi=j;
        cout<<mi<<' '<<i<<endl;
        swap(a[mi],a[i]);
    }
    return 0;
}