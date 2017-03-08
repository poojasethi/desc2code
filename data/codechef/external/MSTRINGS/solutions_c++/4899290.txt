#include <bits/stdc++.h>
using namespace std;
 
#define REP(i,a,b) for(int i=a;i<b;i++)
#define FOR(i,n) REP(i,0,n)
#define REP1(i,a,b) for(int i=a;i<=b;i++)
#define FOR1(i,n) REP1(i,1,n)

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

typedef long long LL;
typedef pair<int,int> ii;

int gcd(int a,int b){
    if(b==0) return a;
    return gcd(b,a%b);
}

 
int main() {
    int t,len;
    scanf("%d",&t);
    char str[20];
    bool pallin;
 
    while(t--){
        scanf("%s",str);

        pallin=true;
        len = strlen(str);
        if(len==1)
            pallin=true;
        
        else{
            for(int i=0;i<len/2;i++){
                if(str[i] == str[len-i-1])
                    continue;
                else{
                    pallin=false;
                    break;
                }
            }
        }

        if(pallin)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}