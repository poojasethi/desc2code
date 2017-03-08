#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define afor(i,N) for(i;i<N;i++)
#define beg ll T;cin>>T;while(T--)

int main(){
beg{
    ll count=0;
    string str,strF="",strop="",strA="";
    stack<char> s;
    cin>>str;
    for(ll i=0;i<str.size();i++){
        if(str[i]=='('){
            count++;
        }
        else if(str[i]==')'){
            cout<<s.top();
            --count;
            s.pop();
        }
        else if(str[i]=='+' || str[i]=='-'||str[i]=='*' ||str[i]=='^' ||str[i]=='!' ||str[i]=='/'  ){
            s.push(str[i]);
            /*if(str[i]=='+' || str[i]=='-'||str[i]=='*' ||str[i]=='^'||str[i]=='%' ||str[i]=='!' ||str[i]=='/'  ){
                strop+=str[i];
            }
            else{
                strA+=str[i];
            }*/
        }
        else{
            cout<<str[i];
        }
    }
    cout<<endl;
}
return 0;
}
