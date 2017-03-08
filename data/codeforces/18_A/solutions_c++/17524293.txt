#include <bits/stdc++.h>
using namespace std;

int x[6];
int c[2];
bool isValid() 
{
    int a = (x[0]-x[2])*(x[0]-x[2]) + (x[1]-x[3])*(x[1]-x[3]);
    int b = (x[2]-x[4])*(x[2]-x[4]) + (x[3]-x[5])*(x[3]-x[5]);
    int c = (x[4]-x[0])*(x[4]-x[0]) + (x[5]-x[1])*(x[5]-x[1]);
    if( !a || !b || !c ) return false;
    if( a==b+c || b==c+a || c==a+b )  return true;
    return false;
}

int main() 
{
    for( int i=0; i<6; i++ ) scanf("%d",&x[i]);
    if( isValid() ) {printf("RIGHT\n");; return 0; }

    c[0]=1;
    c[1]=-1;
    for( int i=0; i<6; i++ ) 
    for( int j=0; j<2; j++ )
    {
        x[i] += c[j];
        if( isValid() ) { printf("ALMOST\n"); return 0; }
        x[i] -= c[j];
    }
    printf("NEITHER\n");
    return 0;
}