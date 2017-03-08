#include <iostream>
#define MAXN 100005
using namespace std;

long long ft[MAXN][12];

int lowbit(int x)
{
    return x&-x;
}

void update(int i, int j, long long v)
{
    for ( ; i < MAXN; i += lowbit(i) )
        ft[i][j] += v;
}

long long sum(int i, int j)
{
    long long result = 0;
    for (; i > 0; i -= lowbit(i) )
        result += ft[i][j];
    return result;
}

int main()
{
    int n, k;
    cin >> n >> k;
    for ( int i = 0; i < n; ++i )
    {
        int a;
        cin >> a;
        update(a, 0, 1);
        for ( int j = 1; j <= k; ++j )
            update(a, j, sum(a-1, j-1));
    }
    cout << sum(MAXN, k) << endl;
    return 0;
}
