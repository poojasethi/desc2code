#include<stdio.h>
#include<string.h>
char dp[51*10001];
int main(void){
	int n,d,sum,k,max,count;
	while(scanf("%d%d",&n,&d)!=EOF){
		memset(dp,0,sizeof(dp));
		dp[0]=1;
		max=count=sum=0;
		while(n--){
			scanf("%d",&k);
			for(int i=sum+=k;i>=k;i--)
				if(dp[i-k]==1)
					dp[i]=1;
		}	
		while(1){
			int j=max+d;
			while(dp[j]==0&&j>max)
				j--;
			if(j==max)
				break;
			max=j;
			count++;	
		}
		printf("%d %d\n",max,count);
	}
	return 0;
}