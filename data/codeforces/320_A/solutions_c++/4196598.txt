#include<stdio.h>

char s[50];

int main(){
	int i;
	scanf("%s", s);
	for(i=0; s[i];){
		if(s[i]!='1'){
			puts("NO");
			return 0;
		}
		if(s[i+1]!='4')i++;
		else if(s[i+2]!='4')i+=2;
		else i+=3;
	}
	puts("YES");
	return 0;
}