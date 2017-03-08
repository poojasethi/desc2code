//Author : pakhandi
//
using namespace std;
 
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<cstring>
 
#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)
#define scan(n) scanf("%d", &n)
#define scans(s) scanf("%s", s)
#define scanc(c) scanf("%c", &c)
#define scanp(f) scanf("%f", &f)
#define scanll(l) scanf("%lld", &l)
#define print(n) printf("%d\n", n)
#define prints(s) printf("%s\n", s)
#define printc(c) printf("%c\n", c)
#define printp(f) printf("%f\n", f)
#define printll(l) printf("%lld\n", l)
#define nline printf("\n")
#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define MOD 1000000007
#define ll long long int
 
int mat[3][2][4]= 
{
  {{10, 15, -25, 1} , {-10, -15, 25, 2}} ,
  {{10, 15, -25, 0} , {-10, -20, 30, 1}} ,
  {{10, 20, -30, 2} , {-10, -15, 25, 0}}
};
 
int main()
{
  int i, j, cases=2, n;
  int temp=0, eb=60, ew=100, eg=160, b, w, g, ele;
 
  	  scan(n);
	  eb=60; ew=100; eg=160;
	  fl(i,0,n)
	  {
	    scan(ele);
		ele--;
	    eb=eb+mat[temp][ele][0];
	    ew=ew+mat[temp][ele][1];
	    eg=eg+mat[temp][ele][2];
	    temp=mat[temp][ele][3];
	  }
	  eb/=10;
	  ew/=10;
	  eg/=10;
	  printf("%d %d %d", eb,ew, eg);
	  nline;
 
  return 0;
} 