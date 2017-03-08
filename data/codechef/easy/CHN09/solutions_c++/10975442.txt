#include <stdio.h>
#include <string.h>

int main(){
	int t;
	int  i;
	int a,b;
	char str[101];
	scanf("%d", &t);
	while(t--){
		scanf("%s", str);
		a = 0;
		b = 0;
		for(i = 0; i < strlen(str); i++){
			if(str[i] == 'a')
				a++;
			else
				b++;
		}
		if(a <= b)
			printf("%d\n", a);
		else
			printf("%d\n", b);
	}
	
	return 0;
}