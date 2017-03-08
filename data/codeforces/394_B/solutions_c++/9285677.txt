#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;
const int MAX =1e6+10;
int A[MAX];
int main() {
	int p,x;
	cin>>p>>x;
	for (int i = x; i < 10; ++i)
	{
		A[1]=i;
		int r=0;
		for (int j = 2; j <=p+1 ; ++j)
		{
			A[j]=(A[j-1]*x+r)%10;
			r=(A[j-1]*x+r)/10;
		}
		if(A[p+1]==A[1] && r==0){
			for (int j = p; j >=1 ; j--)
			{
				cout<<A[j];
			}
			cout<<endl;
			return 0;
		}
	}
	cout<<"Impossible\n";
	return 0;
}