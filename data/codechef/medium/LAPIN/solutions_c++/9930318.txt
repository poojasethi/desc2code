//https://www.codechef.com/problems/LAPIN
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    int t;
    cin>>t;
    while (t--) {
        map<char, int> dict1, dict2;
        map<char, int>::iterator it1, it2;
        string s;
        cin>>s;
        int len = s.length();
        for(int i=0; i<len/2; i++) {
            dict1[s[i]]++;
            dict2[s[len-i-1]]++;
        }
        it1 = dict1.begin();
        it2 = dict2.begin();

        // for(it1 = dict1.begin(); it1 != dict1.end(); it1++, it2++){
        //     if(it1->second != it2->second)
        //         break;
        // }
        // if(it1 == dict1.end() && it2 == dict2.end() && (dict1.size() == dict2.size()))
        //     cout<<"YES"<<endl;
        // else
        //     cout<<"NO"<<endl;

        if (dict1 == dict2)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
}
