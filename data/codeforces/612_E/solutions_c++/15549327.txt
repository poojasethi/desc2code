#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>

using namespace std; 

int p[1000003],n,a[1000003],q[1000003],father[1000003],cnt; 
bool vis[1000003];

int main() {
	scanf("%d",&n); 
	for(int i=1;i<=n;i++) scanf("%d",&p[i]);
	for(int i=1;i<=n;i++)
		if (!vis[i]){
			int len=0;
			for(int k=i;!vis[k];vis[k]=true,len++,k=p[k]); 
			if ( len & 1) {
				cnt+=len; 
				for(int k=0,t=0,v=i;t<len; t++,k=(k+2) % len,v=p[v]) a[k]=v; 
				for(int k=0;k<len;k++) q[a[k]]=a[(k+1)%len];
			}else {
				if (father[len]==0) {
					father[len]=i;
					continue; 
				}
				cnt+=2*len; 
				int u=father[len]; 
				father[len]=0; 
				for(int k=0,t=0,v=i;t<len;k+=2,t++,v=p[v] ) a[k]=v;
				for(int k=1,t=0,v=u;t<len;k+=2,t++,v=p[v]) a[k]=v; 
				for(int k=0;k<2*len;k++) q[a[k]]=a[(k+1) % (2*len)];
			}
		}
	if (cnt<n) cout<<-1<<endl;
	else  for(int i=1;i<=n;i++) printf("%d ",q[i]); 
	return 0; 
}