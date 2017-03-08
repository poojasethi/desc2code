#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	int t,i,j,c,lenk,lenl;
	char k[100000],l[100000];
	scanf("%d",&t);
	while(t--){
		c=i=j=0;
		scanf("%s%s",k,l);
		lenk=strlen(k);
		lenl=strlen(l);
		while(i<lenk){
			if((k[i]==l[j])&&(j<lenl)){
				i++;
				j++;}
			else{
				i++;
				c++;
			}
			if(c>1)
				break;
		}
		if(c>1)
			printf("0\n");
		else
			printf("1\n");
	}
	return 0;
}
