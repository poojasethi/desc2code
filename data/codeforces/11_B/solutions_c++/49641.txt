#include <cstdio>
int x,k=0,p=0;
int main(){
        scanf("%d",&x);
        if(x<0)x=-x;
        while(p<x||(x%2!=0)^(p%2!=0))k++,p+=k;
        printf("%d",k);
        return 0;}