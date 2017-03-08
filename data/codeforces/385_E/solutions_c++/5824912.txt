#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;
typedef __int64 LL;
struct Matrix{
    LL m[7][7];
}E,D,T;
LL mod,sx,sy,dx,dy,t;
void init(){
    for(int i=1;i<=6;i++)
        for(int j=1;j<=6;j++)
            E.m[i][j]=(i==j);
    memset(T.m,0,sizeof(T.m));
    T.m[1][1]=T.m[1][6]=T.m[2][2]=T.m[2][6]=T.m[3][6]=T.m[4][6]=2;
    T.m[1][2]=T.m[1][3]=T.m[1][5]=1;
    T.m[2][1]=T.m[2][4]=T.m[2][5]=1;
    T.m[3][1]=T.m[3][2]=T.m[3][3]=T.m[3][5]=1;
    T.m[4][1]=T.m[4][2]=T.m[4][4]=T.m[4][5]=1;
    T.m[5][5]=T.m[5][6]=T.m[6][6]=1;
}
Matrix multi(Matrix A,Matrix B){
    Matrix ans;
    for(int i=1;i<=6;i++)
        for(int j=1;j<=6;j++){
            ans.m[i][j]=0;
            for(int k=1;k<=6;k++)
                ans.m[i][j]=((ans.m[i][j]+A.m[i][k]*B.m[k][j])%mod+mod)%mod;
        }
    return ans;
}
Matrix Pow(Matrix A,LL k){
    Matrix ans=E;
    while(k){
        if(k&1) k--,ans=multi(ans,A);
        else k/=2,A=multi(A,A);
    }
    return ans;
}
int main(){
    init();
    while(scanf("%I64d%I64d%I64d%I64d%I64d%I64d",&mod,&sx,&sy,&dx,&dy,&t)!=EOF){
        memset(D.m,0,sizeof(D));
        D.m[1][1]=sx-1,D.m[2][1]=sy-1,D.m[3][1]=dx,D.m[4][1]=dy,D.m[5][1]=0,D.m[6][1]=1;
        Matrix ans=multi(Pow(T,t),D);
        printf("%I64d %I64d\n",ans.m[1][1]+1,ans.m[2][1]+1);
    }
    return 0;
}
