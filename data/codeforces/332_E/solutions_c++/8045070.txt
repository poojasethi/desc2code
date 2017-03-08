#include <bits/stdc++.h>
using namespace std;

char s[1000010],t[205];
int n,m,k,an[2010],a[2010],su;
void upd(){
	for(int i = 1;i <= k;i ++){
		if(a[i] < an[i]){
			memcpy(an,a,sizeof(a));
			return;
		}
		if(a[i] > an[i])	return;
	}
}
int check(int i,int j,int o){
	while(j <= n){
		if(i > m || s[i] != t[j])	return 0;
		i += k;
		j += o;
	}
	return i > m;
}

int main(){
	m = 0;
	char ch = getchar();
	while(ch != '\n')	s[++ m] = ch, ch = getchar();
	n = 0;
	ch = getchar();
	while(ch != '\n')	t[++ n] = ch, ch = getchar();
	cin >> k;
	for(int i = 1;i <= k;i ++)	an[i] = 1;
	for(int i = 1;i <= n;i ++){
		int cnt = i,flag = 0;
		for(int j = k;j;j --){
			if(check(j,cnt,i)){
				a[j] = 1;
				cnt --;
				if(!cnt){
					flag = 1;
					for(int o = 1;o < j;o ++)	a[o] = 0;
					break;
				}
			}else	a[j] = 0;
		}
		if(flag){
			su = 1;
			upd();
		}
	}
	if(su)	for(int i = 1;i <= k;i ++)	printf("%d",an[i]);
	else	printf("0\n");
	return 0;
}

