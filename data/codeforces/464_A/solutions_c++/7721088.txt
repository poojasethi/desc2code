#include<cstdio>
#include<cstring>
using namespace std;

int n, p;
char buf[1100];
char add(int i)
{
	for (char ch = buf[i]+1; ch < 'a'+p; ch++) 
		if (ch != buf[i-1] && ch != buf[i-2])
			return ch;
	return 0;
}
int main()
{
	scanf("%d %d %s", &n, &p, buf+2);
	buf[0] = buf[1] = 0;
	for (int i = n+1; i > 1; i--){
		int x = add(i);
		if (x != 0){
			buf[i] = x;
			for (int j = i+1; j <= n+1; j++){
				buf[j] = 'a'-1;
				buf[j] = add(j);
			}
			buf[n+2] = 0;
			printf("%s\n", buf+2);
			return 0;
		}
	}
	puts("NO");
	return 0;
}
