#include<bits/stdc++.h>
using namespace std;
int main(){
	char s[1100000];
	scanf("%s",s);
	int sl=strlen(s);
	int mx=-1;
	for(int i=0;i<sl;i++){
		if((s[i]-'0')%2==0){
			if(s[i]<s[sl-1]){
				mx=i;
				break;
			}
			else
				mx=i;
		}
	}
	if(mx==-1)
		puts("-1");
	else{
		swap(s[mx],s[sl-1]);
		puts(s);
	}
}

