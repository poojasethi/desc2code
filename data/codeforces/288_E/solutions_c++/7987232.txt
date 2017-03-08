#include <iostream>
#include <string>
#define MOD 1000000007ULL
using namespace std;

string l,r;

unsigned long long f(string to)
{
	unsigned long long A,oldA,B,oldB,C,oldC,N,len,a1,an;
	len = to.size();
	A = 0;
	B = 0;
	C = 0;
	N = 1;
	a1=0,an=0;
	for(int i=1;i<=len;i++)
	{
		oldA=A, oldB=B, oldC=C;
		A = ((200*A)%MOD + (220*B)%MOD + (65*N)%MOD)%MOD;
		B = ((20*B)%MOD + (11*N)%MOD)%MOD;
		C = ((100*(oldA+oldC))%MOD + (110*oldB)%MOD + 70*(oldB+MOD-a1)%MOD + 40*(oldB+MOD-an) + (28*(2*N+MOD-1))%MOD)%MOD;
		a1 = (10*a1+4)%MOD;
		if(to[i-1]=='4')
		{
			A = (A+MOD-(100*((an*an)%MOD)+140*an+49)%MOD)%MOD;
			B = (B+MOD-(10*an+7)%MOD)%MOD;
			C = (C+MOD-(100*((an*an)%MOD)+110*an+28)%MOD)%MOD;
			
			an = (10*an+4)%MOD;
			N  = (2*N-1)%MOD;
		}
		else
		{
			an = (10*an+7)%MOD;
			N = (2*N)%MOD;
		}
	}
	
	//cout << A << ' ' << B << ' ' << C << endl;
	return C;
}

int main()
{
	cin >> l >> r;
	cout << (f(r)+MOD-f(l))%MOD << endl;
	return 0;
}

