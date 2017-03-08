#include <stdio.h>
#include <algorithm>
using namespace std;
int h,w,r=-1;
char ans[10][10];
char store[10][10];
char plow[4][3][4]={{"###",".#.",".#."},{"..#","###","..#"},{".#.",".#.","###"},{"#..","###","#.."}};
int mv[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
int best[10][10];
void dfs(int t,int Y,int X){
	if(1<Y&&1<X&&t<best[Y-2][X-2])	return;
	if(1<Y&&1<X)best[Y-2][X-2]=t;
	int ssy=1000,ssx=1000;
	for(int sy=max(0,Y-2);sy+2<h&&sy<ssy+3;sy++)
		for(int sx=0;sx+2<w&&sx<ssx+3;sx++){
			if(store[sy+1][sx+1]!='.')
				continue;
			for(int p=0;p<4;p++){
				int ok=1;
				for(int i=0;i<3&&ok;i++)
					for(int j=0;j<3&&ok;j++)
						if(store[sy+i][sx+j]!='.'&&plow[p][i][j]=='#')
							ok=0;
				if(ok){
					if(ssy==1000)
						ssy=sy,ssx=sx;
					for(int i=0;i<3;i++)
						for(int j=0;j<3;j++)
							if(plow[p][i][j]=='#')
								store[sy+i][sx+j]='A'+t;
					dfs(t+1,sy,sx);
					for(int i=0;i<3;i++)
						for(int j=0;j<3;j++)
							if(plow[p][i][j]=='#')
								store[sy+i][sx+j]='.';
				}
			}
		}
	if(r<t){
		r=t;
		for(int i=0;i<h;i++)
			for(int j=0;j<w;j++)
				ans[i][j]=store[i][j];
	}
}
int main(){
	scanf("%d%d",&h,&w);
	for(int i=0;i<10;i++)
		for(int j=0;j<10;j++){
			ans[i][j]=store[i][j]='.';
			best[i][j]=-1;
		}
	dfs(0,0,0);
	printf("%d\n",r);
	for(int i=0;i<h;i++){
		for(int j=0;j<w;j++)
			printf("%c",ans[i][j]);
		printf("\n");
	}
	return 0;
}

