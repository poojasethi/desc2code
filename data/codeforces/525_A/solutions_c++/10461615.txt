#include<iostream>
#include<cstdio>

int main()
{
	int n,i,count=0,low[30]={0};
	char ch;
	scanf("%d",&n);
	getchar();
	for(i=1;i<n;i++){
		ch=getchar();
		low[ch-'a']++;
		ch=getchar();
		if(low[ch-'A']) low[ch-'A']--;
		else count++;
	}
	printf("%d\n",count);
 return 0;
}

