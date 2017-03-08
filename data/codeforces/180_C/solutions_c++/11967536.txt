#include <bits/stdc++.h>
using namespace std;
#ifdef CORLEONE
  #define d(b) cerr<< #b << " " << b << endl
  #else
  #define d(b)
#endif

using namespace std;

string s;

int main(){
    cin>>s;
    int i,m,ans;
    for(i=m=0;s[i];i++) m+=(s[i]<=96);
    ans=m;
    for(i=0;s[i];i++){
        m-=(s[i]<=96)*2-1;
        if(m<ans) ans=m;
    }
    printf("%d\n",ans);
}