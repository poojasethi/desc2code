#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <utility>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)

using namespace std;

inline void Input(int &N)
{
	int ch;
	N=0;

	while((ch<'0'||ch>'9') && ch!=EOF)
		ch=getchar();

	do
		N=(N<<3)+(N<<1)+(ch-'0');
	while((ch=getchar())>='0' && ch<='9');

	return;
}

/*	Comparing A(p),B(q)
	If A is greater than B only after increment --> p(1-q) = p-pq

	If A is greater than B --> 1-(1-p)q = 1-(q-pq) = 1-q+pq
	Factoring it in terms of (1-q) for cumulative sum
	1(1-q)-p(1-q)+p = 1-q-p+pq+p = 1-q+pq

	If A-D is greater than B --> 1
*/

int N,D;
int ar[50005],lft[25002],rt[25002];
double prob[50005],lPrb[25002],rPrb[25002];

double cum[25002];

double merge(int st,int end)
{
	int mid=(st+end)/2;
	EFOR(l,st,mid)
		lft[l-st]=ar[l],lPrb[l-st]=prob[l];

	EFOR(r,mid+1,end)
		rt[r-mid-1]=ar[r],rPrb[r-mid-1]=prob[r];

	cum[0]=1-rPrb[0];
	for(int a=mid+2,i=1;a<=end;a++,i++)
		cum[i]=cum[i-1]+(1.-rPrb[i]);

	double ans=0;
	int ind,L;
	EFOR(a,st,mid){
		ind=lower_bound(ar+mid+1,ar+end+1,ar[a]+D)-ar;
		ind--,L=ind-mid;
		if(ind>mid)
			ans+=prob[a]*cum[L-1];

		ind=lower_bound(ar+mid+1,ar+end+1,ar[a])-ar;
		ind--,L=ind-mid;
		if(ind>mid)
			ans+=(cum[L-1]-2*prob[a]*cum[L-1]+L*prob[a]);

		ind=lower_bound(ar+mid+1,ar+end+1,ar[a]-D)-ar;
		ind--,L=ind-mid;
		if(ind>mid)
			ans+=(L-cum[L-1]+prob[a]*cum[L-1]-L*prob[a]);
	}

	lft[mid+1-st]=1000000001;
	rt[end-mid]=1000000001;

	int fir=0,sec=0;
	EFOR(all,st,end){
		if(lft[fir]<=rt[sec]){
			ar[all]=lft[fir];
			prob[all]=lPrb[fir++];
		} else {
			ar[all]=rt[sec];
			prob[all]=rPrb[sec++];
		}
	}
	return ans;
}

double msort(int st,int end)
{
	double ret=0;
	if(st<end){
		ret+=msort(st,(st+end)/2);
		ret+=msort((st+end)/2+1,end);
		ret+=merge(st,end);
	}
	return ret;
}

int main()
{
	int T;
	Input(T);
	while(T--){
		Input(N),Input(D);

		FOR(inp,0,N)	Input(ar[inp]);
		FOR(inp,0,N){
			int tmp;
			Input(tmp);
			prob[inp]=tmp/100.;
		}

		double ans=msort(0,N-1);
		printf("%.4lf\n",ans);
	}

	return 0;
}
