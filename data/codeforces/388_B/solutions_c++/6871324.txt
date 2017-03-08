#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

bool a[91][91];

int main(){
    int n;
    scanf("%d", &n);
    for(int i=2;i<60;i++)
        if(i&1) a[i][i+1]=a[i][i+2]=1;
        else a[i][i+2]=a[i][i+3]=1;
    a[0][2]=a[0][3]=a[90][1]=1;
    if(n&1<<29) a[61][1]=1;
    for(int i=62;i<90;i++) a[i][i+1]=1;
    for(int i=0;i<29;i++)
        if(n&1<<i)
            a[i+62][2*i+3]=1;
    printf("%d\n", 91);
    for(int i=0;i<91;i++, putchar(10))
        for(int j=0;j<91;j++)
            printf("%c", a[i][j]|a[j][i]?'Y':'N');
    return 0;
}