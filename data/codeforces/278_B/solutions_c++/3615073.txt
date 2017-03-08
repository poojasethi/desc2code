//278B
#include<stdio.h>
#define MIN(a,b)((a)<(b))?(a):(b)
int main() {
 int n;
 scanf("%d%*c",&n);
 char ct,cp;
 char hash1[26]={};
 char hash2[26][26]={};
 while(n--) {
   cp=getchar()-'a';
   hash1[cp]=1;
   while((ct=getchar())!='\n')
   { hash1[ct=ct-'a']=1;
     hash2[cp][ct]=1;
     cp=ct;
  }
 }
  char *p,*q;
  for(p=hash1,q=p+26;p<q;p++)
    if(*p==0){ putchar(p-hash1+'a'); break; }
  if(p==q)  
    for(p=(char *)hash2,q=p+26*26;p<q;p++)
    if(*p==0) { putchar((p-(char *)hash2)/26+'a'); putchar((p-(char *)hash2)%26+'a'); break;}
  return 0;
}