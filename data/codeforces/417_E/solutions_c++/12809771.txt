#include <bits/stdc++.h>

using namespace std;

int n, m, a[111], b[111];

int main()
{
    cin >> n >> m;
    for (int i = 1; i < n; ++i)
        a[i] = 2;
    for (int i = 1; i < m; ++i)
        b[i] = 2;
    if (n > 2) a[0] = n-2; else if (n == 1) a[0] = 1; else a[0] = 3, a[1] = 4;
    if (m > 2) b[0] = m-2; else if (m == 1) b[0] = 1; else b[0] = 3, b[1] = 4;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
            cout << a[i]*b[j] << ' ';
        cout << endl;
    }

    return 0;
}
