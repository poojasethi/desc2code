#include<cstdio>
int n,m,x,y,p,q,k,flag,t[100010],l[100010],r[100010];
void write(int x){
	if (x==0) printf((flag==1?"R":"L"));else printf("X");
}
int main(){
	scanf("%d%d%d%d",&n,&m,&x,&y);
	for (int i=1;i<=m;i++) scanf("%d%d%d",&t[i],&l[i],&r[i]);
	if (x<y) flag=1;else flag=-1;
	p=x;
	q=1;
	k=0;
	while (1){
		k++;
		while (q<m && t[q]<k) q++;
		if (t[q]!=k || ((p>r[q] || p<l[q]) && (p+flag>r[q] || p+flag<l[q]))){
			p+=flag;
			write(0);
		}else write(1);
		if (y==p) break;
	}
}
