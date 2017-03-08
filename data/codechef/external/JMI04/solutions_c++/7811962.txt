#include <stdio.h>
#include <iostream>

using namespace std;

int main(){

int t,x;
int fib(int x);
cin>>t;

while(t--)
{
cin>>x;


if(fib(x)==1)
printf("Yes\n");
else
printf("No\n");
};






return(0);

};


int fib(int x){


int a = 0;
int b = 1;
int next;

if(x==0||x==1)
return 1;

while(next<=x)
{
next = a + b;
a = b;
b = next;
if(next==x)
return 1;
};
 
return(0);


};