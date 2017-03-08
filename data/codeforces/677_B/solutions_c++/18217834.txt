#include<cstdio>
int main()
{
    //while(1){
    __int64 t,n,k,h,q=0,time = 0;
    scanf("%I64d%I64d%I64d",&n,&h,&k);
    for(int i=0;i<n;++i)
    {
        scanf("%I64d",&t);
        if(q+t<=h) q+=t;
        else {q=t;++time;}
        time+=q/k;
        q%=k;
    }
    if(q) ++time;
    printf("%I64d\n",time);
    return 0;
}
