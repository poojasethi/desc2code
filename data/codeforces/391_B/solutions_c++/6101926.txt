#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

string in;

int ans = 0;

int main(){
    cin >> in;
    for(int x = 0;x<in.length();x++){
        int pos = 1;
        int past = x;
        char cur = in.at(x);
        for(int a = x+1;a<in.length();a++){
            if(in.at(a)==cur&&(a-past)%2==1){
                pos++;
                past = a;
            }
        }
        if(pos>ans){
            ans = pos;
        }
    }
    cout << ans << endl;

    return 0;
}
