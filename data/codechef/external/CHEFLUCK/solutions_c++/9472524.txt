#define gc getchar_unlocked
#define pc putchar_unlocked
#include <iostream>
#include <cstdio>
using namespace std;
typedef long long int lli;
inline int readInt();
inline lli readLong();
inline void printInt(int a);
inline void printLong(lli a);
int main(){
    int t=readInt();
    while (t--) {
        lli n = readLong();
        if (n >= 7) {
            if(n%7==0) {printInt(n);continue;}
            else if(n%7==0 && n%4==0) {printInt(n);continue;}
            else {
                int p=n/7;
                for (int i = p; i >= 0; i--) {
                    if((n-(i*7))%4==0) {
                        printLong((lli)i*7);
                        goto q;
                    }
                }
                printInt(-1);continue;
                q:continue;
            }
        }else {
            if(n==4) printInt(0);else printInt(-1);
            continue;
        }
    }
    return 0;
}
inline int readInt(){
    int n=0; int ch=gc(); int sign=1;
    while( ch < '0' || ch > '9' ){
        if(ch=='-')sign=-1; ch=gc();
    }
    while(  ch >= '0' && ch <= '9' )
        n = (n<<3)+(n<<1) + ch-'0', ch=gc();
    return n*sign;
}
inline void printInt(int a) {
    char snum[20]; int i=0;
    if(a<0) {pc('-'); a=-a;}
    do {
        snum[i++]=a%10+48; a=a/10;
    }
    while(a!=0);
    i=i-1;
    while(i>=0)
        pc(snum[i--]);
    pc('\n');
    //pc(' ');
}
inline lli readLong(){
    lli n=0; lli ch=gc();int sign=1;
    while( ch < '0' || ch > '9' ){
        if(ch=='-')sign=-1; ch=gc();
    }
    while(  ch >= '0' && ch <= '9' )
        n = (n<<3)+(n<<1) + ch-'0', ch=gc();
    return n*sign;
}
inline void printLong(lli a) {
    char snum[50]; lli i=0;
    if(a<0) {pc('-'); a=-a;}
    do {
        snum[i++]=a%10+48; a=a/10;
    }
    while(a!=0);
    i=i-1;
    while(i>=0)
        pc(snum[i--]);
    pc('\n');
    //pc(' ');
}
