#include <bits/stdc++.h>
using namespace std;

#define get(n) scanf("%lld",&n)
#define pii pair<long long, long long>
#define LL long long
#define mp(a,b) make_pair(a,b)
#define ft first
#define sd second
#define F(i,n) for (int i=0; i<n; i++)

LL dist(pii a, pii b)
{
	return (pow((a.ft - b.ft),2) + pow((a.sd-b.sd),2));
}

bool sq(pii a, pii b, pii c, pii d)
{
	LL ab,ac,ad,bc,bd,cd;
	ab = dist(a,b);
	ac = dist(a,c);
	ad = dist(a,d);
	bc = dist(b,c);
	bd = dist(b,d);
	cd = dist(c,d);

	if (ab == ac && bd == cd && ad == 2*ab && bc == 2*ab)
		return true;
	else if (ad == ac && bd == bc && ab == 2*ac && cd == 2*ac)
		return true;
	else if (ad == ab && cd == bc && ac == 2*ab && bd == 2*ab)
		return true;
	else
		return false;
}

int main()
{
	LL n,x,y,a,b,poss;
	get(n);

	pii pt[4][4],c[4];

	F(i,n)
	{
		F(j,4)
		{
			get(x);
			get(y);
			pt[j][0] = mp(x,y);
			get(a);
			get(b);

			c[j] = mp(a,b);

			pt[j][1] = mp(-y+b+a,x-a+b);
			pt[j][2] = mp(-x+2*a,-y+2*b);
			pt[j][3] = mp(y-b+a,-x+a+b);
		}

		LL min = 5555;

		F(q,4)
		{
			F(w,4)
			{
				F(e,4)
				{
					F(r,4)
					{
						if (sq(pt[0][q], pt[1][w], pt[2][e], pt[3][r]))
						{
							if (q+w+e+r < min && pt[0][q] != pt[1][w])
								min = q+w+e+r;
						}
					}
				}
			}
		}

		printf("%lld\n", (min==5555)?-1:min);
	}
}