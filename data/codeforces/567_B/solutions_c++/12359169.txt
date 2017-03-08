#include<stdio.h>
int a[1000008]={0};
int main(){
	int n,i,s=0,ma=0,temp;
	char b[10];
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%s %d",b,&temp);
		if(b[0]=='+'){
			a[temp]++;
			s++;
		}
		else{
			if(a[temp]==0){
				ma++;
			}
			else{
				a[temp]--;
				s--;
			}
		}
		ma=ma>s?ma:s;
	}
	printf("%d\n",ma);

}