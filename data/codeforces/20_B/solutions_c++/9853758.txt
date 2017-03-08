#include<bits/stdc++.h>
long long A,B,C,D;
int main()
{
	std::cin>>A>>B>>C;
	D=B*B-4*A*C;
	if(A==0&&B==0&&C==0)
		printf("-1\n");
	else if(A==0&&B==0&&C!=0)
		printf("0\n");
	else if(A==0)
		printf("1\n%lf\n",-(double)C/B);
	else if(D<0)
		printf("0\n");
	else if(D==0)
		printf("1\n%.9lf\n",-B*1.0/2/A);
	else if(A>0)
		printf("2\n%.9lf\n%.9lf\n",(-B-sqrt(D))*1.0/2/A,(-B+sqrt(D))*1.0/2/A);
	else
		printf("2\n%.9lf\n%.9lf\n",(-B+sqrt(D))*1.0/2/A,(-B-sqrt(D))*1.0/2/A);
	return 0;
}
