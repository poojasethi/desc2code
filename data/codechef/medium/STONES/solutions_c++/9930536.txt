//https://www.codechef.com/problems/STONES
#include <iostream>
#include <string>
#include <map>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--) {
        string s, j;
        cin>>j;
        cin>>s;
        map<char, int> jewel;
        for(int i=0; i<j.length(); i++) {
            jewel[j[i]]++;
        }

        int count=0;
        for(int i=0; i<s.length(); i++) {
            if(jewel[s[i]])
                count++;
        }
        std::cout << count << std::endl;
    }
    return 0;
}
