#include<stdio.h>
struct point{
	int x,y;
}p[10];
int main(){
	int i,j,t,f=1,cnt=0;
	int a[10];
	for(i=0;i<8;i+=2){
		scanf("%d%d%d%d",&p[i].x,&p[i].y,&p[i+1].x,&p[i+1].y);
		if(p[i].x==p[i+1].x)
		    cnt+=1;
		else if(p[i].y==p[i+1].y)
		    cnt+=10;
		else
		    f=0;
		a[i]=a[i+1]=0;
	}
	if(cnt!=22) f=0;
	for(i=0;i<8;i++)
	    for(j=0;j<8;j++)
			if(p[i].x==p[j].x&&p[i].y==p[j].y)
			    a[i]++;
    for(i=0;i<8;i++)
		if(a[i]!=2)
		    f=0;
	puts(f?"YES":"NO");
	return 0;
}