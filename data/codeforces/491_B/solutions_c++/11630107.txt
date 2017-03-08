#include<iostream>
#include<cstdio>
#include<algorithm>
#define N 50001
#define MAXN 2000000000
int n,ans1;
long long ans0,x2,x1,y2,y1;
long long max(long long x,long long y){return x>y?x:y;}
long long min(long long x,long long y){return x<y?x:y;}
long long abs(long long x,long long y){return x<0?-x:x;}
void init(){
    static int x,y;
    x2=y2=MAXN,x1=y1=-MAXN;
    scanf("%d %d",&x,&y);
    scanf("%d",&n);
    for (;n--;){
        scanf("%d %d",&x,&y);
        x2=min(x2,x+y),y2=min(y2,x-y),x1=max(x1,x+y),y1=max(y1,x-y);
    }
    scanf("%d",&n);
}
void work(){
    static bool p;
    static int x,y;
    static long long s;
    p=false;
    for (int i=1;i<=n;i++){
        scanf("%d %d",&x,&y);
        x+=y,y=x-y-y;
        s=max(max(max(abs(x2-x),abs(x1-x)),abs(y2-y)),abs(y1-y));
        if (s<ans0||!p)
            p=1,ans0=s,ans1=i;
    }
}
void write(){
    printf("%I64d\n%d",ans0,ans1);
}
int main(){
    init();
    work();
    write();
    return 0;
}