#define gc getchar_unlocked
#define pc putchar_unlocked
#include<bits/stdc++.h>
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
        pair<lli,lli> p[n];
        for(lli i=0;i<n;i++) {
            lli a = readLong(),x=readLong();
            p[i].second=a,p[i].first=x;
        }
        sort(p,p+n);
        if(n==1 && p[0].first==0) {cout<<0<<endl;continue;}
        for (lli i = n-1; i>=0; i--) {
            if(i!=n-1&&p[i].first!=0) cout<<" + ";
            if (p[i].first > 1) {
                cout<<p[i].second*p[i].first<<"x^"<<p[i].first-1;
            }
            else if (p[i].first == 1) {
                cout<<p[i].second;
            }
            else {break;}
        }
        cout<<endl;
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
