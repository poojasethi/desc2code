#include<cstdio>
using namespace std;
int n,k,i,flag,a[100010],use[100010],sg,j,l;
char ch;
int main()
{
    scanf("%d%d",&n,&k);
    for(i=1;i<=n;i++)
    {
        for(flag=0;ch<'0'&&ch!='-'&&ch!='?';ch=getchar());
        if(ch=='?')use[i]=1,ch=getchar();
        if(ch=='-')flag=1,ch=getchar();
        for(;ch>='0';ch=getchar())a[i]=a[i]*10+ch-'0';
        if(flag)a[i]=-a[i];
    }for(i=1;i<=k;i++)
    {
        a[0]=-1001000000;sg=0;a[n+1]=1001000000;
        for(j=i;j<=n;j+=k)
        {
            if(!use[j])
            {
                if(a[j]-(j-sg)/k<a[sg])
                {
                    puts("Incorrect sequence");
                    return 0;
                }else
                {
                    if(a[j]*2<(j-sg)/k)for(l=j-k;l>sg;l-=k)a[l]=a[l+k]-1;
                    else if(-a[sg]*2<(j-sg)/k)for(l=sg+k;l<j;l+=k)a[l]=a[l-k]+1;
                    else for(l=j-k;l>sg;l-=k)a[l]=l/k-(j+sg)/k/2;
                }sg=j;
            }
        }if(-a[sg]*2<(j-sg)/k)for(l=sg+k;l<j;l+=k)a[l]=a[l-k]+1;else
        {
            if(!sg)sg=i-k;
            for(l=sg+k;l<j;l+=k)a[l]=l/k-(j+sg)/k/2;
        }
    }for(i=1;i<=n;i++)printf("%d ",a[i]);puts("");
}