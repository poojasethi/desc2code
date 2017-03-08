#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <climits>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#define round_int(n) floor(n+0.5)
#define round_up(n,s) round_int(n*pow(10,s))/pow(10,s) 
#define loop(a,s,e) for(a=s;a<=e;a++)
#define lld long long int
#define mod 1000000007
#define array_size(a) (1[&a]-a)
#define debug(format, ...) fprintf(stderr,format,## __VA_ARGS__)
using namespace std;


inline lld input( )
{
    lld n=0;
    lld ch=getchar_unlocked();
    while( ch >= '0' && ch <= '9' )
    n = (n<<3)+(n<<1) + ch-'0', ch=getchar_unlocked();
    return n;
}

inline lld input_gen()
{
	lld t=0;
	char c;
	c=getchar_unlocked();
loop:
	while( (c<'0' || c>'9') && c != '-')
		c=getchar_unlocked();
	int n=0;
	if (c == '-' ) {
		c = getchar_unlocked();
		if (c >='0' && c <= '9')
			n=1;
		else {goto loop;}
	}
	while(c>='0' && c<='9')
	{
		t=(t << 3)+(t << 1)+c-'0';
		c=getchar_unlocked();
	}
	if (n==0)
		return(t);
	else {return (-t);}
}



int main()
{
    lld n,t,c,m,result;
	t=input();
	while(t--)
	{
		c=input();
		result=0;
		while(c--)
		{
			n=input_gen();
			m=input_gen();
			result^=(n+m-2)%3;
		}
		if(result==0)
			printf("Football\n");
		else
			printf("MasterChef\n");
	}

	return 0;
}
