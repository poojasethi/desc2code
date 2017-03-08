#include<cstdio>
#include<cstdlib>

void Get(int &T)
{
	char C;bool F=0;
	for(;C=getchar(),C<'0'||C>'9';)if(C=='-')F=1;
	for(T=C-'0';C=getchar(),C>='0'&&C<='9';T=T*10+C-'0');
	F&&(T=-T);
}

int N,M;
int A[1005];
int B[1005];

void Init()
{
	Get(N);Get(M);
	for(int i=1;i<=N;i++)
	{
		Get(A[i]);
		A[0]+=A[i];
	}
}

void Error()
{
	puts("No");exit(0);
}

void Work()
{
	if(M>A[0]) Error();
	if(M<=0) Error();
	if(N==1&&M!=A[1]) Error();
	
	if(N==1)
	{
		puts("Yes");
		for(int i=1;i<=A[1];i++)
			printf("1 1 ");
		puts("");
		return;
	}
	else
	{
		if(M==1)
		{
			int k=0;
			for(int i=1;i<=N;i++)
				if(A[i]==1)
					k=i;
			if(k==0) Error();
			
			puts("Yes");
			A[k]--;
			printf("%d ",k);
			for(int i=1;i<=N;i++)
				for(int j=1;j<=A[i];j++)
					printf("%d %d ",i,i);
			printf("%d\n",k);
			return;
		}
		else
		{
			puts("Yes");
			A[1]--;A[2]--;
			M-=2;
			for(int i=1;i<=N&&M>0;i++)
				for(;A[i]>0&&M>0;)
				{
					A[i]--;
					M--;
					printf("%d %d ",i,i);
				}
			printf("%d ",1);
			for(int i=2;i<=N;i++)
				for(int j=1;j<=A[i];j++)
					printf("%d %d ",i,i);
			printf("%d ",1);
			printf("%d ",2);
			
			for(int i=1;i<=1;i++)
				for(int j=1;j<=A[i];j++)
					printf("%d %d ",i,i);
			
			puts("2");
		}
	}
}

int main()
{
	Init();
	Work();
	return 0;
}