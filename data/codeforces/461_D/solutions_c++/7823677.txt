#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<cstring>

using namespace std;
typedef long long ll;

int mo=1000000007;
int f[200222],p[200222];
int x,y,m,n,i,z,k;
int xzq;

void Read()
{
	char c;
	while(c=getchar(),c!='x'&&c!='o');
	if(c=='o')k=1;
	else k=0;
}

int find(int r)
{
	if(f[r]==r)return r;
	else f[r]=find(f[r]);
	return f[r];
}

void mi(int x)
{
	if(x==0)return;
	if(x==1){
		xzq=(xzq*2)%mo;
		return;
	}
	mi(x/2);
	xzq=(ll)xzq*xzq%mo;
	if(x%2==1)xzq=(xzq*2)%mo;
}

void add(int x,int y,int k)
{
	int st,ed;
	if(x>y)swap(x,y);
	st=y-x+1;
	ed=st+(min(n-y+1,x)-1)*2;
	st=max(st-2,0);
	if(k==0){
		f[find(f[2*ed+2])]=find(f[2*st+2]);
		f[find(f[2*ed+1])]=find(f[2*st+1]);
	}
	else{
		f[find(f[2*ed+2])]=find(f[2*st+1]);
		f[find(f[2*ed+1])]=find(f[2*st+2]);
	}

}

int main()
{
	scanf("%d%d",&n,&m);
	for(i=1;i<=2*n+2;i++)f[i]=i;
	for(i=1;i<=m;i++){
		scanf("%d%d",&x,&y);
		Read();
		add(x,y,k);
	}
	xzq=1;
	for(i=0;i<=n;i++)if(find(2*i+1)==find(2*i+2))xzq=0;
	for(i=1;i<=2*n+2;i++)p[find(i)]++;
	for(i=1;i<=2*n+2;i++)if(p[i]!=0)z++;
	mi(z/2-1);
	printf("%d\n",xzq);
}