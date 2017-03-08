#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
const int Maxn = 30000005;
int sum[Maxn], son[Maxn][2];
int p[2000005], g[2000005];
int T[2000005];
int l1,r1,l2,r2,n,Q,x,ans,st,i;

void ins(int &p,int q,int l,int r,int pos){
  p = ++st;
  son[p][0] = son[q][0];
  son[p][1] = son[q][1];
  sum[p] = sum[q]+1;
  if (l==r) return;
  int mid = (l+r)>>1;
  if (mid>=pos) ins(son[p][0],son[q][0],l,mid,pos);
    else ins(son[p][1],son[q][1],mid+1,r,pos);
}

int query(int p,int q,int l,int r,int L,int R){
  if (L>r || l>R) return 0;
  if (L<=l && R>=r) return sum[p]-sum[q];
  int mid = (l+r)>>1;
  return query(son[p][0],son[q][0],l,mid,L,R) + query(son[p][1],son[q][1],mid+1,r,L,R);
}

int calc(int x){
  return (x-1+ans)%n+1;
}

int main(){
  scanf("%d",&n);
  for (i=1;i<=n;i++){
    scanf("%d",&x);
    p[x] = i;
  }
  for (i=1;i<=n;i++){
    scanf("%d",&x);
    g[i] = p[x];
  }
  for (i=1;i<=n;i++)
    ins(T[i],T[i-1],1,n,g[i]);
  scanf("%d",&Q);
  while (Q--){
    scanf("%d%d%d%d",&l1,&r1,&l2,&r2);
    int t1=calc(l1), t2=calc(r1);
    l1=min(t1,t2); r1=max(t1,t2);
    t1=calc(l2), t2=calc(r2);
    l2=min(t1,t2); r2=max(t1,t2);
//    printf("%d %d %d %d: ",l1,r1,l2,r2);
    ans = query(T[r2],T[l2-1],1,n,l1,r1);
    printf("%d\n",ans); ans++;
  }
  return 0;
}