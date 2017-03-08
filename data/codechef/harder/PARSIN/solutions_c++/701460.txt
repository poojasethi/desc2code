/*
 * $Date: Wed Oct 12 19:56:30 2011 +0800
 * $Source: Codechef OCT11 PARSIN
 * $Method: Magnificent recurrence + matrix multiplication
 */
#include <cstdio>
#include <cstring>
#include <cmath>

const int M_MAX = 31;

struct Matrix{
	int R, C;
	double ele[2 * M_MAX + 1][2 * M_MAX + 1];
	Matrix(){
		memset(ele, 0, sizeof(ele));
	}
} T, F[2];

Matrix mul(const Matrix &A, const Matrix &B){
	Matrix res;
	res.R = A.R, res.C = B.C;
	for(int i = 1; i <= res.R; i ++)
		for(int j = 1; j <= res.C; j ++){
			res.ele[i][j] = 0;
			for(int k = 1; k <= A.C; k ++)
				res.ele[i][j] += A.ele[i][k] * B.ele[k][j];
		}
	return res;
}

Matrix powMat(const Matrix &A, int n){
	Matrix B = A;
	Matrix res;
	if(n & 1)
		res = B;
	else{
		res.R = res.C = A.R;
		for(int i = 1; i <= res.R; i ++)
			res.ele[i][i] = 1;
	}
	for(n >>= 1; n; n >>= 1){
		B = mul(B, B);
		if(n & 1)
			res = mul(res, B);
	}
	return res;
}

void solve(){
	int N, M;
	double X;
	scanf("%d%d%lf", &M, &N, &X);
	if(N == 1){
		if(M == 1)
			printf("%.6lf\n", sin(X));
		else
			printf("%.6lf\n", 0.0);
		return;
	}
	for(int t = 0; t < 2; t ++)
		memset(F[t].ele, 0, sizeof(F[t].ele));
	memset(T.ele, 0, sizeof(T.ele));
	F[0].R = 2 * M, F[0].C = 1;
	F[0].ele[1][1] = sin(X);
	F[0].ele[M + 1][1] = sin(2 * X);
	F[0].ele[M + 2][1] = sin(X) * sin(X);
	T.R = T.C = 2 * M;
	for(int i = 1; i <= M; i ++){
		T.ele[i][M + i] = 1;
		T.ele[M + i][i] = -1;
		T.ele[M + i][M + i] = 2 * cos(X);
		if(i < M)
			T.ele[M + i + 1][M + i] = sin(X);
	}
	T = powMat(T, N - 2);
	F[1] = mul(T, F[0]);
	printf("%.6lf\n", F[1].ele[2 * M][1]);
}

int main(){
	int T;
	scanf("%d", &T);
	while(T --)
		solve();
}
