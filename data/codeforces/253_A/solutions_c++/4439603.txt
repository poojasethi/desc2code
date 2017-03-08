#include<stdio.h>
#include<iostream>
using namespace std;

int main (){
     freopen("input.txt","r",stdin);
     freopen("output.txt","w",stdout);
int n,m;
cin >> n >> m;

if(m>n){cout <<"G";m--;}
while((n+m)>0)
{
    if(n>0){cout <<"B";n--;}
    if(m>0){cout <<"G";m--;}
}
return 0;}