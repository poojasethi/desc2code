#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
	int i, k, f;
	char s[101], ar[125][4];
	for(i = 0 ; i < 125 ; i++)
		sprintf(ar[i], "%d", i*8);
	scanf("%s", s);
	f = 0;
	for(i = 0 ; i < 125 ; i++){
		k = 0;
		for(int j = 0 ; s[j] != '\0' ; j++){
			if(ar[i][k] == s[j]){
				k++;
				if(ar[i][k] == '\0'){
					f = 1;
					break;
				}
			}
		}
		if(f == 1)
			break;
	}
	if(f == 1)
		printf("YES\n%s", ar[i]);
	else
		printf("NO");
	return 0;
}