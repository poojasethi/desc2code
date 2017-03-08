#include<bits/stdc++.h>

using namespace std;
#define ll long long
#define beg ll T; cin>>T; while(T--)
#define c 0
#define h 1
#define e 2
#define f 3

int main(){
    //beg{
        string str;
        cin>>str;
        ll count[4];
        memset(count,0,sizeof(count));
        for(ll i=0;i<str.size();i++){
            if(str[i]=='C'){
                count[c]++;
            }
            else if(str[i]=='H' && count[c]>count[h]){
                count[h]++;
            }
            else if(str[i]=='E' && count[h]>count[e]){
                count[e]++;
            }
            else if(str[i]=='F'&& count[e]>count[f]){
                count[f]++;
            }
        }
        //sort(count,count+4);
        cout<<count[f];
//}
return 0;
}
