#include<iostream>
using namespace std;
int a[104][104];
int m,n,l;
int main()
{
    cin>>m;
    n=3;
    a[1][2]=1;a[1][3]=1;
    a[2][1]=1;a[2][3]=1;
    a[3][1]=1;a[3][2]=1;
    m--;
    while(m!=0)
    {
        n++;l=1;a[n][1]=a[1][n]=1;
        //cout<<m<<endl;
        while(m>=l&&l<n-1)
        {
            m-=l;l++;
            a[n][l]=a[l][n]=1;
        }
    }
    cout<<n<<endl;
    for(int i=1;i<=n;i++)
    {
       for(int j=1;j<=n;j++)cout<<a[i][j];
       cout<<endl;
    }
    return 0;
}
