#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,i,j;
	double m[200][200];
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		for(j=1;j<=n;j++)
			scanf("%lf",&m[i][j]);
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++)
			printf("%lf ",(m[i][j]+m[j][i])/2);
		printf("\n");
	}
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++)
			printf("%lf ",(m[i][j]-m[j][i])/2);
		printf("\n");
	}
 return 0;
}

