#include <bits/stdc++.h>

using namespace std;

string a, b, buf;

int main()
{
    //freopen("in.txt", "r", stdin);

    cin >> a >> b;
    buf = string(abs((int)b.length() - (int)a.length()), '0');
    if (a.length() < b.length())
        a = buf + a;
    else
        b = buf + b;
    if (a < b)
        cout << '<';
    else if (a == b)
        cout << '=';
    else
        cout << '>';
    return 0;
}
