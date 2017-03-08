#include <cstdio>
#include <cstring>
char s[30],t[30];
int l,a = 0,b = 0,x,y;
int f(char c){
	if (c == '(') return 1;
	if (c == '8') return 2;
	return 0;
}
int main(){
	scanf("%s%s",s,t);
	l = strlen(s);
	for (int i = 0;i < l;i += 2){
		x = f(s[i]);
		y = f(t[i]);
		if (x == y) continue;
		if ((x + 1) % 3 == y) a++;else b++;
	}
	if (a > b) printf("TEAM 1 WINS\n");
	else if (a < b) printf("TEAM 2 WINS\n");
	else printf("TIE\n");
}
