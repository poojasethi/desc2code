#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
  int t,i,a,b;
  char arr[101];
  scanf("%d",&t);
  while(t--)
  {
    scanf("%s",arr);
    a=0;b=0;
    for(i=0;i<strlen(arr);i++)
    {
      if(arr[i]=='a') 
        a++;
      else
        b++;     
    }
    printf("%d\n",(a>=b)?(b):(a));
  }
}