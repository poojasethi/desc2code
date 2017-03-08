#include <stdio.h>
#include <string.h>
int main(){
	int r,n,q[105],xx;
	char s[105];
	scanf("%d",&n);
	while(n--){
		scanf("%s",s);
		r=0;
		xx=0;
		for(int i=0;i<strlen(s);i++){
			if(s[i]==':'){
				q[++r]=i;
				if(i>0)if(s[i-1]==':')	xx=r-1;
				//printf("///%d %d\n",i,xx);
			}
		}
		//printf("**%d\n",r);
		q[0]=-1;
		q[++r]=strlen(s);
		for(int i=0;i<r;i++){
			//printf("(%d)",i);
			if(xx==i){
				if(r>8)continue;
				for(int j=1;j<=8-r;j++)printf("0000:");
			}
			for(int j=1;j<=5-q[i+1]+q[i];j++)printf("0");
			for(int j=q[i]+1;j<q[i+1];j++)printf("%c",s[j]);
			printf("%c",i==r-1?'\n':':');
		}
	}
	return 0;
}