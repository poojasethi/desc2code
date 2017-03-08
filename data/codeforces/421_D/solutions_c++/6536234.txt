#include <iostream>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <utility>
using namespace std;

map<pair<int,int>,int> MAP;
int a[300005]={0},b[300005]={0};
int main()
{
    int n,p;
    long long sum=0;
    pair<int,int> tmp;
    cin >> n >> p ;
    for(int i=0;i<n;i++)
    {
        scanf("%d%d",&tmp.first,&tmp.second);
        if(tmp.first>tmp.second) swap(tmp.first,tmp.second);
        MAP[tmp]++;
        a[tmp.first]++;a[tmp.second]++;
        b[tmp.first]++;b[tmp.second]++;
    }
    sort(b+1,b+n+1);
    for(int i=n;i>0;i--)
    {
        sum+=i-(lower_bound(b+1,b+i,p-b[i])-b);
    }
    map< pair<int, int>, int>::iterator it;
    for(it=MAP.begin(); it!=MAP.end(); ++it)
    {
        int x=it->first.first, y=it->first.second;
        int tmp= it->second;
        if(a[x]+a[y]>=p && a[x]+a[y]-tmp<p) sum--;
    }
    cout << sum ;
    return 0;
}
