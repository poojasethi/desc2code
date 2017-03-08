#include <bits/stdc++.h>
using namespace std;
long long n,avg,r,i,rez,sum;
pair <long long, long long> a[100500];
int main()
{
    cin>>n>>r>>avg;

    for (i = 0; i < n; i++)
    {
        cin>>a[i].second>>a[i].first;
        sum += a[i].second;
    }
    sort(a,a+n);
    rez = i = 0;
    while (sum < avg*n)
    {
        long long tmp = min(avg*n-sum,r-a[i].second);
        rez += tmp*a[i].first;
        sum += tmp;
        i++;
    }
    cout<<rez;
    return 0;
}