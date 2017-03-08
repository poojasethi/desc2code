#include <cstdio>
#include <sstream>
#include <cstring>
using namespace std;
int a[30]={ 0,2, 6, 14, 30, 62, 126, 254, 510, 1022, 2046, 4094, 8190, 16382, 32766, 65534, 131070, 262142, 524286, 1048574, 2097150, 4194302, 8388606, 16777214, 33554430, 67108862, 134217726, 268435454, 536870910, 1073741822 };

int getchar_unlocked() { return getchar(); }
inline void fastRead_string(char *str)
{
    register char c = 0;
    register int i = 0;
    while (c < 33)    c = getchar_unlocked();
    while (c != '\n') {  str[i] = c;
        c = getchar_unlocked();
        i = i + 1;      }
    str[i] = '\0';
}

int main() {
	register int i,x,y;bool s7=false;
	scanf("%d",&x);
	for(i=0;i<32;i++){
		if(a[i]>=x) break;
	}
	while(i>=1){
		if(x>(a[i]+a[i-1])/2)  {s7=true; printf("7");  }
		else { printf("4"); s7=false;}
		x-=s7?(a[i]-a[i-1]):(a[i]-a[i-1])/2;
		i--;
	}
	return 0;
}