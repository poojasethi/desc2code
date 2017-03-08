# include <stdio.h>

int n,m;

char S[509][509];

int F[1000009][4],a;

int X[] = {0 , 0 , -1 , 1};
int Y[] = {1 , -1 , 0 , 0};

void dfs(int x,int y,int p)
{
	F[a][0] = 1; F[a][1] = x; F[a++][2] = y;
	
	S[x][y] = '#';
	
	for(int h=0; h<4; h++)
	{
		int x1 = x + X[h];
		int y1 = y + Y[h];
		
		if(S[x1][y1] == '.')	dfs(x1,y1,1);
	}
	
	if(p != -1)
	{
		F[a][0] = 3 , F[a][1] = x , F[a++][2] = y;
		F[a][0] = 2 , F[a][1] = x , F[a++][2] = y;
	}
}

int main()
{
	scanf("%d %d",&n,&m);
	
	for(int h=1; h<=n; h++)
	{
		scanf("%s",S[h]);
		for(int j=m; j>0; j--)	S[h][j] = S[h][j-1];
		S[h][0] = '#';
	}
	
	for(int h=1; h<=n; h++)
		for(int j=1; j<=m; j++)
			if(S[h][j] == '.')	dfs(h,j,-1);
	
	printf("%d\n",a);
	
	for(int h=0; h<a; h++)
	{
		if(F[h][0] == 1)	printf("B ");
		if(F[h][0] == 2)	printf("R ");
		if(F[h][0] == 3)	printf("D ");
		printf("%d %d\n",F[h][1],F[h][2]);
	}
}
