#include <cstdio>
#include <algorithm>
using namespace std;
double dp[10][10][10];
int a[10][2];
int n;
int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;++i){
		scanf("%d%d",&a[i][0],&a[i][1]);
	}
	double expectation = 0;
	for(int b=1;b<=10000;++b){
		for(int i=0;i<10;++i)for(int j=0;j<10;++j)for(int k=0;k<10;++k)dp[i][j][k]=0;
		dp[0][0][0] = 1.0;
		for(int i=1;i<=n;++i){
			for(int j=0;j<=n;++j){
				for(int k=0;k<=n;++k){
					double prob = 1.0/(a[i][1]-a[i][0]+1);
					double temp = 0;
					//lower
					temp = dp[i-1][j][k] * (min(b-a[i][0], a[i][1]-a[i][0]+1)) * prob;
					if(temp < 0) temp = 0;
					dp[i][j][k] += temp;
					temp = 0;
					//equal
					if(a[i][0] <= b && b <= a[i][1])
						if(j>0)
							dp[i][j][k] += dp[i-1][j-1][k] * prob;
					//higher
					if(k>0)temp = dp[i-1][j][k-1] * (min(a[i][1]-b, a[i][1]-a[i][0]+1)) * prob;
					if(temp < 0) temp = 0;
					dp[i][j][k] += temp;
				}
			}
		}
		for(int j=1;j<=n;++j){
			expectation += 1.0 * b * dp[n][j][1];
			if(j>1) expectation += 1.0 * b * dp[n][j][0];
		}
	}
	printf("%.12lf\n",expectation);
	return 0;
}