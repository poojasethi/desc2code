#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
    int n;
    string c, s;
    cin >> n;
    c += "<3";
    for(int i=0;i<n;i++) 
    {
        cin >> s;
        c += s+"<3";
    }
    cin >> s;
    int idx=0;
    for(int i=0;i<s.size();i++) if(c[idx] == s[i]) idx++;
    cout << (idx == c.size() ? "yes": "no") << endl;
    return 0;
}
