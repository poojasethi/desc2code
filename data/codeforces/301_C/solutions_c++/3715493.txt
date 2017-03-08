#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int i;
int main(){
	for(i='0';i<='9';++i)printf("??%c>>%c??\n",i,i);
	puts("??>>?");
	for(i='0';i<'9';++i)printf("%c?<>%c\n",i,i+1);
	puts("9?>>?0");
	puts("?<>1");
	puts(">>??");
}