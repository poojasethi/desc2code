#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long int
using namespace std;

int MOD = 26;
ll fib[89];

void pre()
{
    int i,x;
    fib[1]=1;
    fib[2]=1;
    for(i=3;i<89;i++)
    {
        x=fib[i-1]+fib[i-2];
        if(x>26) x-=26;
        fib[i]=x;
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    int i,t,n;
    pre();
    cin>>t;
    while(t--)
    {
        cin>>n;
        for(i=1;i<=n;i++)
            cout<<(char)(fib[i]-1+'A');
        cout<<endl;
    }
    return 0;
}
