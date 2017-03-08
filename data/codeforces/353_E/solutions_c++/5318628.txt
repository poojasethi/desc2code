#include<string.h>
#include<stdio.h>
char s[1000010];

int main()
{
    int i,len,max;
    memset(s,0,sizeof(s));
    scanf("%s", s);
    len= strlen(s);
    s[len]  =s[0];
    s[len+1]=s[1];
    s[len+2]=s[2];
    max = 0;
    for(i=0;i<len;i++){
        if(s[i] != s[i+1]){   //01     10
				if(s[i+2]!=s[i]) max++;//011   100  
		   else if(s[i+3]!=s[i]) max++,i++;//010_1    101_0
        }//011  100  010  101    middle
    }
    printf("%d\n",max);
	return 0;
}