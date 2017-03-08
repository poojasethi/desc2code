#include<bits/stdc++.h>
using namespace std;
#define ll long long
 
int main(){
   ll t,n;
   scanf("%lli",&t);
   while(t--){
   scanf("%lli",&n);

   if(n%26!=0)
   printf("%lli\n",n/26+1);

   else
   	printf("%lli\n",n/26);
   
   
   }
   
 
 
 return 0;
} 