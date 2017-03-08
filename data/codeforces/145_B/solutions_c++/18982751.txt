#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int a1,a2,a3,a4;scanf("%d%d%d%d",&a1,&a2,&a3,&a4);
	if (abs(a3-a4)>1) {puts("-1");return 0;}
	if (min(a1,a2)<max(a3,a4)) {puts("-1");return 0;}
	if (a1==a2&&a2==a3&&a3==a4) {puts("-1");return 0;}
	if (a1==a3&&a1==a4)
	{
		for (int i=0;i<a1;i++) printf("74");
		for (int i=0;i<a2-a1;i++) putchar('7');
		return 0;
	}
	if (a3<a4) {putchar('7');a2--;a4--;}
	if (a3==a4)
	{
		for (int i=0;i<a1-a3;i++) putchar('4');
		for (int i=0;i<a3-1;i++) printf("74");
		for (int i=0;i<a2-a3+1;i++) putchar('7');
		puts("4");
		return 0;
	}
	for (int i=0;i<a1-a3+1;i++) putchar('4');
	for (int i=0;i<a4;i++) printf("74");
	for (int i=0;i<a2-a4;i++) putchar('7');
	return 0;
}
