#include<cstdio>
#define MAXN 100010
#define min(x,y) (x<y?x:y)
struct t{int s,p;t(){};t(int _s,int _p){s=_s;p=_p;};};
int n0,x,y,l;t a[MAXN],*ea=a,*b=a+MAXN-1,*eb=b,*pa,*pb;
main(){
  scanf("%d",&n0);
  for(int i=1;i<=n0;++i)
    scanf("%d%d",&x,&y),
    x?*(ea++)=t(y,i):*(eb--)=t(y,i);
  b=eb+1,eb=a+MAXN;
  for(pa=a,pb=b;pa!=ea&&pb!=eb;++pa)
    if (!pa->s)
      printf("%d %d 0\n",pa->p,pb->p);
    else while(pa->s){
      l=min(pa->s,pb->s);
      pa->s-=l;pb->s-=l;
      printf("%d %d %d\n",pa->p,pb->p,l);
      if (pa->s) ++pb;
    }
  for(--pa,++pb;pb!=eb;++pb) printf("%d %d 0\n",pa->p,pb->p);
}