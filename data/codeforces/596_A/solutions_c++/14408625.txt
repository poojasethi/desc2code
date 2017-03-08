#include<bits/stdc++.h>
using namespace std;
int ara[5],ara1[5];
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>ara[i]>>ara1[i];

    sort(ara,ara+n);
    sort(ara1,ara1+n);

    int x=abs(ara[n-1]-ara[0]);
    int y=abs(ara1[n-1]-ara1[0]);
    if(x==0||y==0)
        cout<<-1<<endl;
    else
        cout<<x*y<<endl;
}
