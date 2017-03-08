#include<cstdio>
#include<cstring>
char s[1010],t[1010];
int a[27]={0},b[27]={0},n,m,x,y,l;
int f(int k){
	int s=0;
	for (int i=1;i<=26;i++)
		if (a[i]){
			s+=a[i]/k;
			if (a[i]%k) s++;
		}
	return s;
}
int main(){
	scanf("%s",s);
	l=strlen(s);
	for (int i=0;i<l;i++) a[s[i]-96]++;
	scanf("%d",&n);
	x=0;
	for (int i=1;i<=26;i++) if (a[i]) x++;
	if (x>n){
		printf("-1\n");
		return 0;
	}
	for (int i=1;i<=l;i++)
		if (f(i)<=n){
			x=n-f(i);
			printf("%d\n",i);
			for (int j=1;j<=26;j++)
				if (a[j]){
					y=a[j]/i;
					if (a[j]%i) y++;
					while (y--) printf("%c",j+96);
				}
			while (x--) printf("z");
			printf("\n");
			return 0;
		}
}
