#include <iostream>

using namespace std;

string a, b="";
int i, j, k, t, SIZE;
bool change;

main()
{
    cin >> a >> k;
    SIZE=a.size();
    for (i=0; i < SIZE; i++)
    {
        j=i;
        for (t=i+1; t <= min(i+k, SIZE-1); t++)
            if (a[t] > a[j]) j=t;
        b+=a[j];
        k-=j-i;
        for (t=j; t >= i+1; t--) swap(a[t], a[t-1]);
    }
    cout << b;
}
