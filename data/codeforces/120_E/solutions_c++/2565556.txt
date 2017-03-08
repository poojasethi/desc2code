#include<cstdio>
int n,C;
void doit(){
    scanf("%d",&n);
    printf("%d\n",n&1?0:1);
    }
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&C);
    for(int i=0;i<C;++i)doit();
    }
