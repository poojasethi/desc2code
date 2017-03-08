#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <list>
using namespace std;
 
int main() {
	int t,ans,k,count=0,A[26],B[26],C[26],D[26],num,val;
	 
	int num1,num2,num3,num4,j;
	 
	scanf("%d\n",&t);
	string s;
	while(t--) {
		 
		cin>>s;
		k=s.length();
		memset(A,0,sizeof A);
		memset(B,0,sizeof B);
		memset(C,0,sizeof C);
		memset(D,0,sizeof D);
		 
		count=0;
		 
		for(int i=0;i<k;i++) {
			if(s[i]=='#')
				count++;
		}
		 
		if(count<3) {
			printf("0\n");
			continue;
		}
		 
		j=0; //chusko be
		 
		while(s[j]!='#') {
			A[s[j]-'a']++;
			j++;
		}
		j++;
		 
		while(s[j]!='#') {
			B[s[j]-'a']++;
			j++;
		}
		j++;
		 
		while(s[j]!='#') {
			C[s[j]-'a']++;
			j++;
		}
		j++;
		num=j;
		 
		for(;j<k;j++)
			if(s[j]!='#')
				D[s[j]-'a']++;
		
		ans=0;
		 
		 
		for(int l=0;l<count-2;l++) {
			num1=0;
			num2=0;
			num3=0;
			num4=0;
		 
			for(int i=0;i<26;i++)
				num1=max(num1,A[i]);
			 
			for(int i=0;i<26;i++)
				num2=max(num2,B[i]);
			 
			for(int i=0;i<26;i++)
				num3=max(num3,C[i]);
			 
			for(int i=0;i<26;i++)
				num4=max(num4,D[i]);
			 
			//cout<<j<<" :\n";
			//cout<<num1<<" "<<num2<<" "<<num3<<" "<<num4<<endl<<endl;
			 
			if(num1==0 || num2==0 || num3==0 || num4==0)
				;
			else
				ans=max(ans,num1+num2+num3+num4+3);
			 
			if(l==count-3)
				break;
			 
			for(int i=0;i<26;i++) {
				A[i]+=B[i];
				B[i]=C[i];
			}
			 
			memset(C,0,sizeof C);
		 
			while(s[num]!='#') {
				C[s[num]-'a']++;
				num++;
			}
			num++;
			 
			for(int i=0; i<26;i++)
				D[i]-=C[i];
		}
		 
		printf("%d\n",ans);
	 
	}
	return 0;
}