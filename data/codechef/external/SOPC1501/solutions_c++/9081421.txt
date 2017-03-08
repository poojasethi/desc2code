#include<iostream>
using namespace std;
int main()
{
    int x,y;
    cin>>x>>y;
    int f[y+1];
    f[0]=0;
    f[1]=1;
    for(int i=2;i<y;i++)
    {

        if(i%2==0)
        {
            f[i]=f[i/2];
        }
        else
        {
            f[i]=f[i/2]+1;
        }
    }
    int m=-1000000000;
    for(int i=x;i<y;i++)
    {
        if(m<f[i])
        {
            m=f[i];
        }
    }
    cout<<m<<"\n";
}
