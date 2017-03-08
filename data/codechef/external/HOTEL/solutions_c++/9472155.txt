#define gc getchar_unlocked
#define pc putchar_unlocked
#include <iostream>
#include <utility>
#include <algorithm>
using namespace std;
inline int readInt();
inline void printInt(int a);
int main(){
    int t=readInt();
    while (t--) {
        int n = readInt();
        /*pair<int,int> p[n];
        for(int i=0;i<n;i++) p[i].second = readInt();
        for(int i=0;i<n;i++) p[i].first = readInt();
        if(n==1) {printInt(1);pc('\n');continue;}
        sort(p,p+n);
        int temp =0,ans=0;
        for (int i = 0; i < n;i++) {
            temp =0;
            for (int j = i; j < n; j++) {
                if(p[i].first>p[j].second) temp+=1;
            }
            ans = (temp>ans)?temp:ans;
        }
        printInt(ans);pc('\n');*/
        int a[1010]={0},x;
        for(int i=0;i<n;i++) {x=readInt(); a[x]+=1;}
        for(int j=0;j<n;j++) {x=readInt(); a[x]-=1;}
        int temp=0,ans=a[0];
        for (int i = 1; i < 1001; i++) {
            temp+=a[i];
            ans=(temp>ans)?temp:ans;
        }
        printInt(ans);pc('\n');
    }
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
    //pc('\n');
    pc(' ');
}