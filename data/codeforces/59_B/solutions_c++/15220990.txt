#include <bits/stdc++.h>

using namespace std;
int main() 
{	
	int n,sum=0,minOdd=102,a;
	scanf("%d",&n);
	for(int i=0; i<n; i++)
	{
		scanf("%d",&a);
		sum+=a;
		if(a&1) minOdd=min(minOdd,a);
	}
	if(sum&1) return printf("%d\n",sum),0;
	sum-=minOdd&1?minOdd:sum;
	return printf("%d\n",sum), 0;
}