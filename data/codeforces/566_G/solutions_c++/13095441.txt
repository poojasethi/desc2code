#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define n   100005
#define I64 long long
#define For(i,a,b)  for(int i=a;i<=b;i++)

int     N,M,T,MaxY;

struct  Nod{
        int x,y;

        void    Rd()    {scanf("%d%d",&x,&y);}
        Nod operator -  (const Nod&a)   {return (Nod){x-a.x,y-a.y};}
        I64 operator *  (const Nod&a)   {return 1ll*x*a.y-1ll*y*a.x;}
}A[n],B[n],S[n];

bool    Cmp(const Nod&a,const Nod&b)    {
        return  a.x<b.x||a.x==b.x&&a.y>b.y;
}
bool    cmp(const Nod&a,const Nod&b)    {
        return  a.x<b.x;
}

bool    check(Nod a){
        if  (a.x<S[1].x)    return  a.y>=MaxY;
        if  (a.x>=S[T].x)   return  1;
        int t=upper_bound(S+1,S+T+1,a,cmp)-S-1;
        return  (a-S[t+1])*(S[t]-S[t+1])>=0;
}

int     main(){
        scanf("%d%d%*d%*d",&N,&M);
        For(i,1,N)  A[i].Rd();
        For(i,1,M)  B[i].Rd();
        sort(B+1,B+M+1,Cmp);

        For(i,1,M)  {
            for (;T&&B[i].y>=B[T].y;T--);   B[++T]=B[i];
        }   M=T;    T=0;

        For(i,1,M)  if  (i==1||B[i].x!=B[i-1].x){
            for (;T>1&&(S[T-1]-B[i])*(S[T]-B[i])>=0;T--);
            S[++T]=B[i];
        }
        For(i,1,T)  MaxY=max(MaxY,S[i].y);
        For(i,1,N)  if  (check(A[i]))   return  puts("Max"),0;
        puts("Min");
}