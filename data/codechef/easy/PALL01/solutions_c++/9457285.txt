/*
 * author: jachermocilla@gmail.com
 * url: 
 */


#include <iostream>
#include <sstream>
#include <string>

#define ull unsigned long long

using namespace std;

int main(){
    ull T, input;
    ull i,j,k;
    string s;

    cin >> T;
    for (i=0;i<T;i++){
        cin >> s;
        //cout << s << endl;
        k=s.size();
        for(j=0;j<k/2;j++){
            if (s.at(j) != s.at((k-1)-j)){
                break;
            }
        } 
        if (j==k/2)
            cout << "wins" << endl;
        else
            cout << "losses" << endl;
    }
}
