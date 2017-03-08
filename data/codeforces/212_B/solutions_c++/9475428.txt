#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,m;
char s[1000006];
char s2[100];
short c[1<<26];
int a[10005],b[10005];
int main(){
    scanf("%s%d",s+1,&m);
    n=strlen(s+1);
    int cnt=0;
    for(int i=1;i<=m;i++){
        scanf("%s",s2);
        for(int j=0;s2[j];j++){
            a[i]|=(1<<(s2[j]-'a'));
        }
        if(!c[a[i]]) c[a[i]]=++cnt;
    }
    for(int i=1;i<=n;i++){
        for(int j=i,k=0;j<=n;j++){
            if(s[j]==s[i-1]) break;
            k|=1<<(s[j]-'a');
            if(!(k&(1<<(s[j+1]-'a')))) b[c[k]]++;
        }
    }
    for(int i=1;i<=m;i++) printf("%d\n",b[c[a[i]]]);
    return 0;
}