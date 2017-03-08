#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n, a, b;
    map<int, int> x;
    map<int, int> y;
    cin>>n;
    while(n--)
    {
        cin>>a>>b;
        x[a]++;
        y[b]++;
    }

    cout<<min(x.size(), y.size())<<endl;
    return 0;
}
