# include <stdio.h>
# include <string.h>

int n,m,a,p,b;

int T[1<<19];

void upd(int x,int y,int l,int r,int node)
{
	if(l == r)	{T[node] = y; return ;}
	
	if(x <= (l+r)/2)	upd(x,y,l,(l+r)/2,node*2);
	else 	upd(x,y,(l+r)/2+1,r,node*2+1);
	
	a++;
	
	if(a % 2)	T[node] = T[node*2] | T[node*2+1];
	else	T[node] = T[node*2] ^ T[node*2+1];
}

int main()
{
	scanf("%d %d",&n,&m);
	
	for(int h=0; h<1<<n; h++)	scanf("%d",&p) , a = 0 , upd(h+1,p,1,1<<n,1);
	
	for(int h=0; h<m; h++)	scanf("%d %d",&b,&p) , a = 0 , upd(b,p,1,1<<n,1) , printf("%d\n",T[1]);
}
