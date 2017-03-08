#include <bits/stdc++.h>
using namespace std;
vector<pair<int,int> >qu;
int n;
int kn[8][2]={1,2,1,-2,-1,2,-1,-2,2,1,-2,1,2,-1,-2,-1};
int brd[1001][1001];
int is_safe(int x,int y){
  int m=qu.size();
  for(int i=0;i<m;i++){
    int dx=x-qu[i].first,dy=y-qu[i].second;
    if(abs( dx)==abs(dy) )
      return 0;
  }
  return 1;
}

int is_forked(int x,int y){
  int fork=0;
    for(int j=0;j<8;j++){
      int xx=x+kn[j][0],yy=y+kn[j][1];
      if(xx>=0 && xx<n && yy>=0 && yy<n && brd[xx][yy])
	fork++;
    }
  if(fork>=2)
    return 1;
  else
    return 0;
}


int main(){
  int t;
  scanf("%d",&t);
  while(t--){
    int m;
    int r[1001]={0};
    int c[1001]={0};
    qu.clear();
    scanf("%d%d",&n,&m);
    memset(brd,0,sizeof(brd));
    int x,y;
    for(int i=0;i<m;i++){
      scanf("%d%d",&x,&y);
      x--,y--;
      brd[x][y]=1;
      r[x]=1;
      c[y]=1;
      qu.push_back(make_pair(x,y));
    }
    int ans=0;
    for(int i=0;i<n;i++)
      for(int j=0;j<n;j++)
	if(r[i]==0 && c[j]==0 && is_safe(i,j) && is_forked(i,j))
	  ans++;
    printf("%d\n",ans);
  }
}

