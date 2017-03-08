/*
 * Nimesh Ghelani (nims11)
 * Note: I(Vy) is using his file to test the solution.
 * */
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<map>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<utility>
#define in_T int t;for(scanf("%d",&t);t--;)
#define in_I(a) scanf("%d",&a)
#define in_F(a) scanf("%lf",&a)
#define in_L(a) scanf("%lld",&a)
#define in_S(a) scanf("%s",&a)
#define newline printf("\n")
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define SWAP(a,b) {int tmp=a;a=b;b=tmp;}
#define P_I(a) printf("%d",a)
int n,ans=0,i,j;
long long w,x;
int main()
{
    in_I(n);in_L(w);
    int arr[n];
    for(i=0;i<n;i++)
    {
        in_I(arr[i]);
    }
    long long a = (w*(w-1)*(2*w-1))/6;
    long long b = (w*(w-1))/2;
    long long sumn = 0,sumnsqr = 0;
    for(int i = 0;i<w;i++)
    {sumn+=arr[i];
        sumnsqr += arr[i]*(long long)arr[i];}
    if((sumn-b)%w == 0)
    {
        x = (sumn-b)/w;
        if(sumnsqr == (w*x*x + a + 2*x*b))
            ans++;
    }

    for(int i = w; i<n; i++)
    {
        sumn += arr[i] - arr[i-w];
        sumnsqr += arr[i]*(long long)arr[i] - arr[i-w]*(long long)arr[i-w];
        if((sumn-b)%w == 0)
        {
            x = (sumn-b)/w;
            if(sumnsqr == (w*x*x + a + 2*x*b))
                ans++;
        }
    }
    P_I(ans);
    newline;
}
