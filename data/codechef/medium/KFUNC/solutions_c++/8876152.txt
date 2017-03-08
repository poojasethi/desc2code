#include<bits/stdc++.h>
using namespace std;
long long int digitsum(long long int n)
{
    return (n-1)%9+1;
}
long long int getsum(long long int n,long long int ind,long long int check[])
{
    long long int sum=0,sumtot=0;
    if(n==0)
    {
        return sumtot;
    }
    for(long long int i=0;i<ind;i++)
        sum=sum+check[i];
    sumtot=sum*(n/ind);
    //cout<<sumtot<<"--sumtot[0]\n";
    if((n%ind)!=0)
    {
        for(int i=0;i<(n%ind);i++)
            sumtot=sumtot+check[i];
    }
    return sumtot;
}

int main()
{
    long long int t,n,sum,a,d,l,r;
    long long int check[10],ind;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld %lld %lld %lld",&a,&d,&l,&r);
        check[0]=digitsum(a);
        //cout<<check[0]<<"--check[0]\n";
        ind=1;
        a=a+d;
        sum=digitsum(a);
        while(check[0]!=sum)
        {
            check[ind]=sum;
            ind++;
            //cout<<check[ind-1]<<"--check[ind-1]\n";
            //cout<<ind<<"--ind\n";
            a=a+d;
            sum=digitsum(a);
        }
        printf("%lld\n",getsum(r,ind,check)-getsum(l-1,ind,check));
    }
    return 0;
}
