#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<fstream>

using namespace std;

int x[1001];
int y[1001];

int main()
{
    //freopen("C:\\Users\\Anick\\Desktop\\in.txt","r",stdin);
    //freopen("C:\\Users\\Anick\\Desktop\\out.txt","w",stdout);

    int t;
    for(scanf("%d",&t);t>0;t--)
    {
        long long int n,nik,foo;
        cin>>n;
        for(int i=1;i<=n;i++)
            scanf("%d%d",&x[i],&y[i]);

        if(n%2)
        {
            cout<<"1"<<endl;
            continue;
        }

        sort(&x[1],&x[n+1]);
        sort(&y[1],&y[n+1]);

        nik=abs(x[n/2]-x[n/2 + 1]);
        nik++;
        foo=abs(y[n/2]-y[n/2 + 1]);
        foo++;

        cout<<(foo*nik)<<endl;
    }
}
