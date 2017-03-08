#include <iostream>
using namespace std;
int v[100][100],n,i,j,p;
int main()
{
    cin>>n;
    for(i=1; i<=n; i++)
        for(j=1; j<=n; j++)
        {
            cin>>v[i][j];
            if(v[i][j]==n-1)
                p=i;
        }
    for(j=1;j<=n;j++)
    {
        if(v[p][j]==0)
            cout<<n<<' ';
        else
        cout<<v[p][j]<<' ';
    }
}
