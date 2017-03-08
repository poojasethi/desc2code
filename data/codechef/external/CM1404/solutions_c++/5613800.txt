/*
	Author   : Sandeep Ravindra
	Contest  :
	Problem  :
*/

#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<vector>

using namespace std;

#define	    ll		    long long

#define     s(n)	    scanf("%d",&n)
#define     ss(n)	    scanf("%s",n)
#define     sc(n)	    scanf("%c",&n)
#define     sl(n)	    scanf("%ld",&n)
#define     sll(n)	    scanf("%lld",&n)

#define     fr(i,a,b)	    for(int i=a;i<b;i++)

#define     max(a,b)	    ((a)>(b)?(a):(b))
#define     min(a,b)	    ((a)<(b)?(a):(b))

#define	    p(n)	    printf("%d",n)
#define	    pl(n)	    printf("%ld",n)
#define	    pll(n)	    printf("%lld",n)
#define	    pbl(n)	    printf("\n")

#define     TEST            int _t; s(_t); while(_t--)


int main()
{
	#ifndef ONLINE_JUDGE
		freopen("in.txt","r",stdin);
	#endif
	int c[1005] = {};
	fr(i,0,1003)
        c[i] = i*(i+1)/2, c[i]++;
    TEST
    {
        int n;
        s(n);
        if(n == 1)
            printf("0\n");
        else if(n==2)
            printf("1\n");
        else
        {
            fr(i,1,1003)
                if(n<=c[i+1] && n>c[i])
                {
                    p(i+1),pbl();
                    break;
                }
        }
    }
return 0;
}
