#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int N = 40;

int n, m, r, k, a, b;
ll cnt;
int in[N], i, j;
vector<int> S[N];

int nice(int x)
{
    int ans = 1;
    for(int p=2;p*p<=x;p++)
        if(x%p == 0)
        {
            ans *= p;
            while(x%p == 0) x /= p;
        }
    ans *= x;
    return ans;
}

int main()
{
    scanf(" %d%d%d%d", &n, &k, &a, &b);
    for(i=0;i<n;i++) scanf(" %d", in+i);
    for(i=0;i<n;i++) in[i] = nice(in[i]);

    m = (n+1)>>1;
    r = n-m;

    for(int s=0;s<(1<<m);s++)
    {
        int loc = 0, t = 0;
        for(i=0;i<m;i++) if(s&(1<<i)) loc += in[i], t++;
        S[t].push_back(loc);
    }
    for(i=0;i<N;i++) sort(S[i].begin(), S[i].end());

    for(i=0;i<r;i++) in[i] = in[m+i];
    for(int k=1;k<=::k;k++)
    {
        for(int s=0;s<(1<<r);s++)
        {
            int loc = 0, t = 0;
            for(i=0;i<r;i++) if(s&(1<<i)) loc += in[i], t++;

            if(t > k) continue;

            int aux = upper_bound(S[k-t].begin(), S[k-t].end(), b-loc) -
                      lower_bound(S[k-t].begin(), S[k-t].end(), a-loc);

            cnt += ll(max(aux, 0));
        }
    }
    printf("%lld\n", cnt);
}
