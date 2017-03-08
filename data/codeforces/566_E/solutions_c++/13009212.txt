#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
#include<map>
#include<bitset>

#define N 1005
#define K 28

#define mk make_pair

using namespace std;
map<pair<int,int>,int>mp;
vector<int>v[N];
bitset<N>Bian[N],E;
const int lim=36;
int i,j,m,n,p,k,Pow[lim+5],Q[N],f,x,size[N],Count[N];
void add(int x,int y)
{
	  if (mp[mk(x,y)]) return;
	 v[x].push_back(y);
	 v[y].push_back(x);
	 mp[mk(x,y)]=mp[mk(y,x)]=1;
	 size[x]++;
	 size[y]++;
	 Bian[x][y]=Bian[y][x]=1;
}
struct bit{
	  int bit[lim+1];
	  void ins(int x)
	  {
	  	  bit[(x-1)/K+1]|=Pow[(x-1)%K+1];
	  }
	  void getans()
	  {
	  	 	Q[0]=0;
	  	 	int i,j;
	  	 	for (i=1;i<=lim;++i)
	  	 	      if (bit[i])
	  	 	         for (j=1;j<=K;++j)
	  	 	           if (bit[i]&Pow[j])
	  	 	           {
	  	 	               Q[++Q[0]]=(i-1)*K+j;
	  	 	               if (Q[0]>2) return;
	  	 	           }
	  	    for (i=1;i<=Q[0];++i)
	  	       for (j=i+1;j<=Q[0];++j) add(Q[i],Q[j]);
	  }
	  int Find(int x)
	  {
	  	 return bit[(x-1)/K+1]&Pow[(x-1)%K+1];
	  }
}a[N],C;   
void Pt1()
{
	  for (i=2;i<=n;++i) printf("1 %d\n",i);
	  exit(0);
}
void Pt2()
{
	  Q[0]=0;
	  for (i=1;i<=n;++i) if (size[i]) Q[++Q[0]]=i;
	  printf("%d %d\n",Q[1],Q[2]);
	  for (i=1;i<=n;++i) 
	     if (Count[i]!=n)
	  {
	  	   for (j=1;j<=n;++j)
			   if (!size[j]&&a[i].Find(j)) size[j]=1,printf("%d %d\n",Q[1],j);
		   break;
	  }
	  for (i=1;i<=n;++i)
	    if (!size[i]) printf("%d %d\n",Q[2],i);
	  exit(0);
}
void get(int x)
{
	  int i,j;
	  for (i=1;i<=lim;++i) C.bit[i]=Pow[K+1]-2;
	  for (i=1;i<=n;++i)
	    if (a[i].Find(x)) for (j=1;j<=lim;++j) C.bit[j]&=a[i].bit[j];
	  Q[0]=0;
	  for (i=1;i<=n;++i) if (size[i]&&C.Find(i)) Q[++Q[0]]=i;
	  if (Q[0]==2) printf("%d %d\n",x,(size[Q[1]]==1?Q[1]:Q[2]));
	  else 
	  {
	  	   for (i=1;i<=n;++i) E[i]=0;
	  	   for (i=1;i<=Q[0];++i) E[Q[i]]=1;
	  	   for (i=1;i<=Q[0];++i) if ((E&Bian[Q[i]])==E) break;
	  	   printf("%d %d\n",x,Q[i]);
	  }
}
int main()
{
	 scanf("%d",&n);
	 Pow[0]=1; for (i=1;i<lim;++i) Pow[i]=Pow[i-1]*2;
	 for (i=1;i<=n;++i)
	 {
	 	  scanf("%d",&k);
	 	  if (k!=n) f=1; Count[i]=k;
	 	  for (;k--;) scanf("%d",&x),a[i].ins(x);
	 }
	 if (!f) Pt1();
	 for (i=1;i<=n;++i)
	 {
	 	  for (j=i+1;j<=n;++j)
	 	     {
	 	     	 for (k=1;k<=lim;++k) C.bit[k]=a[i].bit[k]&a[j].bit[k];
	 	     	 C.getans();
	 	     }
	 }
	 for (i=1;i<=n;++i) if (size[i]) f++;
	 if (f==3) Pt2();
	 for (i=1;i<=n;++i) Bian[i][i]=1;
	 for (i=1;i<=n;++i)
	   for (j=0;j<(int)v[i].size();++j) if (i<v[i][j]) printf("%d %d\n",i,v[i][j]);
	 for (i=1;i<=n;++i) if (!size[i]) get(i); 
}