#include<stdio.h>
#include<string.h>
#define M 100005
struct node{
	int from,to,next,flag;
}edge[M*10];
int head[M],tot,Intime,cnt;
int depth[M],mlink[M];
bool bridge;
void add(int a,int b){
	edge[tot].to=b,edge[tot].from=a,edge[tot].next=head[a];
	edge[tot].flag=0,head[a]=tot++;
}
inline int Min(int a,int b){
	return (a<b?a:b);
}
void Tarjan(int k,int fa){
	if(bridge)return;
	depth[k]=mlink[k]=++Intime;
	for(int i=head[k];i!=-1;i=edge[i].next){
		int y=edge[i].to;
		if(depth[y]==0){
		    if(!edge[i^1].flag)edge[i].flag=1;
			Tarjan(y,k);		
			mlink[k]=Min(mlink[y],mlink[k]);
			if(mlink[y]>depth[k]){
				bridge=true;
				return;
			}
		}else if(y!=fa){
			if(!edge[i^1].flag)edge[i].flag=1;
			mlink[k]=Min(mlink[k],depth[y]);
		}
	}
}
int main(){
	int n,m;
	int i,j,k,a,b,c;
	while(scanf("%d %d",&n,&m)!=EOF){
		for(i=1;i<=n;i++){
			head[i]=-1;
			depth[i]=0;
		}
		tot=Intime=0;
		while(m--&&scanf("%d %d",&a,&b)){
			add(a,b);
			add(b,a);
		}
		bridge=false;
		Tarjan(1,0);
		if(bridge)puts("0");
		else{
			for(i=0;i<tot;i++)
				if(edge[i].flag)printf("%d %d\n",edge[i].from,edge[i].to);
		}
	}
	return 0;
}