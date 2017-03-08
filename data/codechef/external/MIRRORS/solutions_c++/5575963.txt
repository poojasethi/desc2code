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

#define     fall(i,a,b)	    for(int i=a;i<b;i++)

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
    TEST
    {
        int m,n;
        s(n),s(m);
        char a[1000][1000]={};
        getchar();
        fall(i,0,n)
        {
            char ch;
            fall(j,0,m)
            {
                ch=getchar();
                a[i][j]=ch;
            }
            getchar();
        }
        fall(i,0,n)
        {
            for(int j=m-1;j>=0;j--)
            {
                printf("%c",a[i][j]);
            }
            pbl();
        }
    }
return 0;
}
