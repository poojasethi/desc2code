#include<bits/stdc++.h>
using namespace std;
int main()
{
	long int n,i,sum= 0,l = 0,r= 0;
	cin>>n;
	vector <long int>tasks(n);
	for (i=0;i<n;i++)
	{
		cin>>tasks[i];
		sum += tasks[i];
	}
	sum /= n;
	for(i=0;i<n;i++)
	{
		if(tasks[i]<sum){
			l += sum - tasks[i];
		}
		else if(sum < tasks[i]){
			r+= tasks[i] - sum - 1;
		}
	}
	cout<<max(l,r);
	return 0;
}
