#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,m;
int d[1000006];
int H[1000006],X[1000006*2],P[1000006*2],tot;
inline void add(int x,int y){
	P[++tot]=y;X[tot]=H[x];H[x]=tot;
}
int cnt=0;
bool vis[1000006];
bool odd[1000006];
void dfs(int x){
	vis[x]=1;
	if(d[x]&1) odd[cnt]=1;
	for(int i=H[x];i;i=X[i]){
		if(!vis[P[i]]) dfs(P[i]);
	}
}
int ans;
int main(){
	scanf("%d%d",&n,&m);
	for(int i=0,x,y;i<m;i++){
		scanf("%d%d",&x,&y);
		d[x]++;d[y]++;
		add(x,y);
		add(y,x);
	}
	for(int i=1;i<=n;i++){
		if(d[i]&&!vis[i]) cnt++,dfs(i);
		ans+=d[i]&1;
	}
	if(cnt==1){
		ans/=2;
		if(ans==0){
			if(!d[1]){
				ans+=2;
			}
		}else if(!d[1]) ans++;
		printf("%d\n",ans);
	}else if(cnt>1){
		ans/=2;
		if(!d[1]) ans++;
		for(int i=1;i<=cnt;i++) if(!odd[i]) ans++;
		printf("%d\n",ans);
	}else puts("0");
	
	return 0;
}