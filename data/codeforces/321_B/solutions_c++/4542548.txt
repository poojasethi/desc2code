#include<cstdio>
#include<cstring>
#include<algorithm>
int a[110],b[110],f[110],n,m,p,q,x,k,ans=0,ans1=0;
bool v[110]={0};
char s[10];
bool flag=1;
bool cmp(int a,int b){
	return (a>b);
}
int main(){
	scanf("%d%d",&n,&m);
	p=q=0;
	for (int i=1;i<=n;i++){
		scanf("%s%d",s,&x);
		if (s[0]=='A'){
			p++;
			a[p]=x;
		}else{
			q++;
			b[q]=x;
		}
	}
	for (int i=1;i<=m;i++) scanf("%d",&f[i]);
	std::sort(a+1,a+p+1);
	std::sort(b+1,b+q+1);
	std::sort(f+1,f+m+1);
	k=0;
	for (int i=1;i<=q;i++){
		while (k<=m&&(f[k]<=b[i]||v[k])) k++;
		if (k>m){
			flag=0;
			break;
		}
		v[k]=1;
	}
	k=0;
	for (int i=1;i<=p;i++){
		while (k<=m&&(f[k]<a[i]||v[k])) k++;
		if (k>m){
			flag=0;
			break;
		}
		ans+=(f[k]-a[i]);
		v[k]=1;
	}
	if (flag) for (int i=1;i<=m;i++) if (!v[i]) ans+=f[i];
	std::sort(f+1,f+m+1,cmp);
	for (int i=1;i<=m && i<=p && f[i]>a[i];i++) ans1+=(f[i]-a[i]);
	if (ans<ans1) ans=ans1;
	printf("%d",ans);
}
