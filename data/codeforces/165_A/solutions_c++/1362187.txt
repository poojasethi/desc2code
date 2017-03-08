#include <stdio.h>
int x[300],y[300];
int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		scanf("%d%d",x+i,y+i);
	int ans=0;
	for(int i=0;i<n;i++){
		int t=0;
		for(int j=0;j<n;j++){
			if(x[i]==x[j]&&y[i]<y[j])	t|=1;
			if(x[i]==x[j]&&y[i]>y[j])	t|=2;
			if(x[i]<x[j]&&y[i]==y[j])	t|=4;
			if(x[i]>x[j]&&y[i]==y[j])	t|=8;
		}
		if(t==15)
			ans++;
	}
	printf("%d\n",ans);
	return 0;
}

