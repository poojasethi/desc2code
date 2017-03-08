#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i,k,cnt=1;
    string str;
    set<char> s;
    cin>>k>>str;
    for(i=0;i<str.size();i++) s.insert(str[i]);
    if(k>s.size()){return puts("NO");}
    s.clear();
    puts("YES");
    for(i=0;i<str.size();i++){
        if(i&&!s.count(str[i])&&cnt<k) puts(""),cnt++;
        printf("%c",str[i]);
        s.insert(str[i]);
    }
}
