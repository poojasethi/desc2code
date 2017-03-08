#include <iostream>

using namespace std;
long long n,i,j,s,v[110],w[110];
char c;
int main()
{
    cin>>n;
    for(i=1;i<=n;i++)
    for(j=1;j<=n;j++)
    {
        cin>>c;
        if(c=='C')
            v[i]++,w[j]++;
    }
    for(i=1;i<=n;i++)
        s+=v[i]*(v[i]-1)/2+w[i]*(w[i]-1)/2;
    cout<<s;
}
