#include<iostream>

using namespace std;

int main(){
int n,m,a,b;
cin>>n>>m>>a>>b;
cout<<min((n/m)*b+min((n%m)*a,b),a*n);
}