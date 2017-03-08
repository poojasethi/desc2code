#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<bitset>
#include<set>
#include<stack>
#include<queue>
#include<deque>
using namespace std;
typedef int MT[100][100];
typedef int MM[100];
typedef long long LL;
int n,C,K,size;
int S[10],M[10];
//0..K ==== g[i][0..k]
//K+1..K+K ==== f[i][K+1..K+k][colors that do not exist.]
//(x+1)*K+1..K ==== f[i][(x+1)*K+1..k][x=color]
MM f,nf;
int c[10],cnt;
MT mat,nmat;
const long long mo = 1000000007;
void ksm(int n){
	while (n){
		if (n & 1){
			memset(nf,0,sizeof(nf));
			for (int i = 0;i <= size;i++)
				for (int j = 0;j <= size ;j++)
					nf[i] = (nf[i]+(LL)mat[i][j]*f[j])%mo;
			for (int i = 0;i <= size ;i++) f[i] = nf[i];
		}
		n >>= 1;
		memset(nmat,0,sizeof(nmat));
		for (int i = 0;i <= size; i++)
			for (int j = 0;j <= size ;j++){
				LL tt = 0;
				for (int k = 0;k <= size ;k++)
					(tt += (LL)mat[i][k]*mat[k][j])%=mo;
				nmat[i][j] = tt;
			}
		for (int i = 0;i <= size ;i++)
			for (int j = 0;j <= size ;j++) mat[i][j] = nmat[i][j];
	}
}
void DP(){
	size = 2*K;
	cnt = 0;
	for (int i = 1;i <= n;i++){
		int pos = -1;
		for (int j = 1;j <= cnt;j++)
			if (S[i] == c[j]) {pos = j;break;}
		if (pos == -1){
			c[++cnt] = S[i];
			pos = cnt;
			for (int j = 1;j <= K;j++)
				f[++size] = f[K+j];//Add more matrix value
		}
		memset(mat,0,sizeof(mat));
		mat[0][0] = 1;
		for (int k = 1;k <= K;k++){
			// Deal with G
			mat[k][k] = 1;// + G[n][k]
			for (int j = 1;j <= cnt;j++)
				if (j != pos)
					mat[k][(j+1)*K+k] = 1;// +F[n][k][c[j]]
			mat[k][K+k] = C-cnt; // + (C-cnt)*F[n][k][not exist.]
			// Pay attation to this: every color that doesn't exist have the same DP value!
			// Deal with colors that do not exist.
			if (cnt < C){//Do not meet all
				int pp = K + k;
				mat[pp][pp] = 1;// F[n][k][not exist.]
				mat[pp][k - 1] = 1;// G[n][k-1]
				if (k > 1){
					for (int j = 1;j <= cnt;j++)
						mat[pp][(j+1)*K+k-1] = 1; // + F[n][k][c[j]]
					mat[pp][K+k-1] = C-cnt-1; // (C-cnt-1)*F[n][k][not exist]
				}
			}// If meet all , cannot add this to result.
			// Deal with colors in it
			for (int j = 1;j <= cnt;j++){
				int pp = (j+1)*K+k;
				mat[pp][pp] = 1;
				if (j != pos){
					mat[pp][k - 1] = 1;// + G[n][k-1]
					if (k > 1){
						for (int jj = 1;jj <= cnt;jj++)
							if (jj != j)// Pay attention to this.
								mat[pp][(jj+1)*K+k-1] = 1;
						mat[pp][K+k-1] = C-cnt;
					}
				}
			}
		}
		ksm(M[i]);
	}
}
int main(){
	int TT;scanf("%d",&TT);
	while (TT--){
		scanf("%d%d%d",&n,&C,&K);
		for (int i = 1;i <= n;i++)
			scanf("%d%d",&S[i],&M[i]);
		memset(f,0,sizeof(f));
		for (int i = 0;i <= K;i++)
			f[i] = 1;
		DP();
		int ans = (f[K]+(LL)(C-cnt)*f[2*K])%mo;
		for (int j = 1;j <= cnt;j++)
			ans = (ans+f[(j+1)*K+K])%mo;
		printf("%d\n",ans);
	}
	return 0;
}
  