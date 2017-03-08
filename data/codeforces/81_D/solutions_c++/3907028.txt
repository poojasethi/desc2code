// 选出的东西头尾也算相邻
#include<cstdio>

#define ran 1111

int n,m,last;
int v[ran],ans[ran];

int main(){
	scanf("%d%d",&n,&m);
	v[0]=0;
	for(int i=1;i<=m;i++)
		scanf("%d",&v[i]);
	last=-1;
	for(int i=0;i<n;i++){
		int id=0;
		for(int j=1;j<=m;j++){
			if(j==last || i==n-1&&j==ans[0])
				continue;
			if(v[j]>v[id])id=j;
			if(v[j]==v[id] && j==ans[0])
				id=j;
		}
		if(!v[id]){
			printf("-1\n");
			return 0;
		}
		v[id]--;
		ans[i]=id;
		last=id;
	}
	for(int i=0;i<n;i++)
		printf("%d%c",ans[i],i<n-1?' ':'\n');

	return 0;
}