#include<bits/stdc++.h>
using namespace std;
char getch(char x,char y){
    for(char a='a';a<='z';a++) if(a!=x&&a!=y) return a;
}
int main()
{
    int i,n,t,q=0,k;
    string s1,s2;
    cin>>n>>t>>s1>>s2;k=n-t;
    for(i=0;i<n;i++) if(s1[i]==s2[i]) q++;
    if(k<=q){
        for(i=0;i<n;i++)
            if(s1[i]==s2[i]&&k){
                printf("%c",s1[i]);k--;
            }else printf("%c",getch(s1[i],s2[i]));
    }else{
        int a=0,b=0;
        string ans;
        for(i=0;i<n;i++)
            if(s1[i]==s2[i]){
                ans+=s1[i];
            }else{
                if(a<k-q) ans+=s1[i],a++;
                else if(b<k-q) ans+=s2[i],b++;
                else ans+=getch(s1[i],s2[i]);
            }
        if(a!=k-q||b!=k-q) puts("-1");
        else cout<<ans;
    }
}
