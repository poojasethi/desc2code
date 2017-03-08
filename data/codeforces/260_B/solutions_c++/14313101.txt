#include <cstdio>
#include <cctype>
#include <cstring>
char str[100005];
int month[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
int cnt[4][16][32];
int main() {
	int d = -1, m = -1, y = -1, id, ansd = 0;
	scanf("%s", str);
	int len=strlen(str);
	for(int i=0;i<len-9;i++) {
		if(isdigit(str[i])&&isdigit(str[i+1])&&
			isdigit(str[i+3])&&isdigit(str[i+4])&&
			isdigit(str[i+6])&&isdigit(str[i+7])&&
			isdigit(str[i+8])&&isdigit(str[i+9])&&
			str[i+2]=='-'&&str[i+5]=='-') {
			d=(str[i+0]-48)*10+str[i+1]-48;
			m=(str[i+3]-48)*10+str[i+4]-48;
			y=(((str[i+6]-48)*10+str[i+7]-48)*10+str[i+8]-48)*10+str[i+9]-48;
			if(m>12||y<2013||y>2015||m<1)continue;
			if(d>month[m]||d<1)continue;
			if(++cnt[y-2013][m][d]>ansd)ansd=cnt[y-2013][m][d],id=i;
		}
	}
	for(int i=0;i<10;i++)putchar(str[id+i]);
	return 0;
}