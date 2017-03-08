#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;
queue<int> qu[200010];
int a[200010],order[200010];

int main()
{
	int i,n,p=0,num=0,m=0;
	scanf("%d",&n);
	for(i=1;i<=n;i++){
		scanf("%d",&a[i]);
		qu[a[i]].push(i);
		//m=max(m,a[i]);
	}
	for(i=1;i<=n;i++){
		if(p>=0&&!qu[p].empty()){
			order[i]=qu[p].front();
			qu[p].pop();
		}
		else{
			printf("Impossible\n");return 0;
		}
		p++;
		while(p>=3&&qu[p].empty()) p-=3;
		//while(p>=3&&!qu[p-3].empty()) p-=3;
	}
	printf("Possible\n");
	for(i=1;i<=n;i++)
		printf("%d ",order[i]);
 return 0;
}

