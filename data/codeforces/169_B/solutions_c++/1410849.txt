#include <iostream>
#include <algorithm>
using namespace std;
string a, s;
int main() {
    cin>>a>>s;
    sort(s.rbegin(), s.rend());
    int sp=0;
    for (int i=0; i<a.length(); i++) {
        if (sp<s.length()&&s[sp]>a[i]) {
            a[i]=s[sp];
            sp++;
        }
    }
    cout<<a<<endl;
}
