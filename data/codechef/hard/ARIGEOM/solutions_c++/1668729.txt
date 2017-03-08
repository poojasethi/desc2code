#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define LL long long

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

int N;
int seq[10002],indx[100002],used[10002];

int AP[10002],GP[10002];
void printSeq()
{
	int A=0,G=0;
	EFOR(i,1,N){
		if(used[i]&1)		AP[A++]=seq[i];
		if(used[i]&2)		GP[G++]=seq[i];
	}

	FOR(i,0,A)		printf("%d ",AP[i]);	printf("\n");
	FOR(i,0,G)		printf("%d ",GP[i]);	printf("\n");
}

void markGP(int a,LL num,LL den)
{
	for(LL val=a;val<=seq[N];val=(val*num)/den){
		if(indx[val]==0)		return;

		used[indx[val]]^=2;
		if((val*num)%den)
			return;
	}
}

void markAP(int a,int d)
{
	for(;a<=seq[N];a+=d){
		if(indx[a]==0)		return;

		used[indx[a]]^=1;
	}
}

void findNonUsed(int &g1,int &g2)
{
	EFOR(i,1,N){
		if(!used[i] && g1==-1)		g1=i;
		else if(!used[i]){
			g2=i;
			return;
		}
	}
}

void reduce(int &num,int &den)
{
	int gcd=__gcd(num,den);
	num/=gcd,den/=gcd;
}

int kthRoot(int val,int k)
{
	int root=int(pow(val+0.,1./k)+1e-11);
	int pwr=int(pow(root+0.,k)+1e-11);

	return (val==pwr)?root:-1;
}

bool isRemnAP(int a1,int a2)
{
	if(a1==-1){
		used[1]|=1,used[2]|=1;
		return 1;
	} else if(a2==-1){
		a1-=(a1==N);
		used[a1]|=1,used[a1+1]|=1;
		return 1;
	} else {
		int a=seq[a1],dif=seq[a2]-seq[a1];

		for(int q=1;q<=5;q++){
			if(dif%q==0){
				markAP(a,dif/q);

				int chk1=-1,chk2;
				findNonUsed(chk1,chk2);
				if(chk1==-1)
					return 1;

				markAP(a,dif/q);
			}
		}
	}
	return 0;
}

bool isRemnGP(int g1,int g2)
{
	if(g1==-1){
		used[1]|=2,used[2]|=2;
		return 1;
	} else if(g2==-1){
		g1-=(g1==N);
		used[g1]|=2,used[g1+1]|=2;
		return 1;
	} else {
		int a=seq[g1],rN=seq[g2],rD=seq[g1];
		reduce(rN,rD);

		for(int rt=1;rt<=12;rt++){
			int nm=kthRoot(rN,rt);
			int dn=kthRoot(rD,rt);

			if(nm!=-1 && dn!=-1){
				markGP(a,nm,dn);

				int chk1=-1,chk2;
				findNonUsed(chk1,chk2);
				if(chk1==-1)
					return 1;

				markGP(a,nm,dn);
			}
		}
	}
	return 0;
}

bool isGP(int g1,int g2)
{
	int nm=seq[g2],dn=seq[g1];
	reduce(nm,dn);
	markGP(seq[g1],nm,dn);

	int a1=-1,a2=-1;
	findNonUsed(a1,a2);

	if(isRemnAP(a1,a2)){
		printSeq();
		return 1;
	}
	return 0;
}

bool isAP(int a1,int a2)
{
	markAP(seq[a1],seq[a2]-seq[a1]);
	int g1=-1,g2=-1;
	findNonUsed(g1,g2);

	if(isRemnGP(g1,g2)){
		printSeq();
		return 1;
	}
	return 0;
}

int main()
{
	int T;
	Input(T);
	while(T--){
		Input(N);

		MEM(indx,0);
		EFOR(i,1,N){
			Input(seq[i]);
			indx[seq[i]]=i;
		}

		EFOR(fr,1,2)	EFOR(sc,fr+1,3){
			MEM(used,0);
			if(isAP(fr,sc)){
				fr=3;
				break;
			}
			MEM(used,0);
			if(isGP(fr,sc)){
				fr=3;
				break;
			}
		}
	}
	return 0;
}
