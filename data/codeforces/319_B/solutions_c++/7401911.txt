#include <bits/stdc++.h>
#define MX 111111
using namespace std;
int p[MX], s[MX], f[MX];
int main()
{
    int n, top = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &p[i]);
    for (int i = n - 1; i >= 0; --i)
    {
        int t = 0;
        while (top && p[s[top - 1]] < p[i])
            f[i] = t = max(t + 1, f[s[--top]]);
        s[top++] = i;
    }
    printf("%d", *max_element(f, f + n));
    return 0;
}