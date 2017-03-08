#include <iostream>
#define MOD 1000000007LL
using namespace std;

int gcd(int a, int b)
{
	if(b==0)
		return a;
	return gcd(b, a%b);
}

int main()
{
	int w,h;
	cin >> w >> h;
	w++, h++;
	
	long long res = 0;
	
	for(int x0=0;x0<2;x0++)
		for(int y0=0;y0<2;y0++)
			for(int x1=0;x1<2;x1++)
				for(int y1=0;y1<2;y1++)
					for(int x2=0;x2<2;x2++)
						for(int y2=0;y2<2;y2++)
							if(((x1-x0)*(y2-y0)-(x2-x0)*(y1-y0))%2==0)
							{
								long long z0 = ((w+1-x0)/2)*((h+1-y0)/2),
									z1 = ((w+1-x1)/2)*((h+1-y1)/2),
									z2 = ((w+1-x2)/2)*((h+1-y2)/2);
								res += ((z0*z1)%MOD)*z2%MOD;
							}
	
	long long r;
	for(int a=0;a<w;a++)
		for(int b=0;b<h;b++)
		{
			if(a==0 && b==0)
				continue;
			
			r=gcd(a,b)-1;
			r=((r*(w-a)%MOD)*(h-b)*((a&&b)?12:6))%MOD;
			
			res = (res-r+MOD)%MOD;
		}
		
	long long s = w*h;
	res = (res-s+MOD)%MOD;
	res = (res-s*(s-1)*3+MOD)%MOD;
	cout << (res+MOD)%MOD << endl;
	return 0;
}

