#include<iostream>
#include<sstream>
using namespace std;

int main() {
    int len;
    cin >> len;
    string s;
    stringstream ss;
    for(int i = 1; i <= 500; i++)   {
        ss << i;
    }
    ss >> s;
    cout << s[len-1];
}
