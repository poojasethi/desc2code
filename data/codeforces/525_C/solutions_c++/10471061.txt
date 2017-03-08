#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

 bool cmp(int x,int y)
 {
	 return x>y;
 }

int main()
{
	int n,i,e,a[100011];
	long long sum=0;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		scanf("%d",&a[i]);
	sort(a+1,a+n+1,cmp);
	e=-1;
	for(i=1;i<n;i++)
		if(a[i]==a[i+1]||a[i]==a[i+1]+1){
			if(e==-1) e=a[i+1];
			else{
				sum+=(long long)e*a[i+1];
				e=-1;
			}
			i++;
		}
	printf("%I64d\n",sum);
 return 0;
}

