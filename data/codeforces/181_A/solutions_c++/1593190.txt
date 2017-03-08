#include<iostream>
using namespace std;
#define N 105
char c[N];
int n,m;
int main()
{
    cin>>n>>m;
    int x,y;
    x=y=0;
    for(int i=0;i<n;i++)
    {
        cin>>c;
        for(int j=0;j<m;j++)
        if(c[j]=='*')
           x^=i,y^=j;
    }
    cout<<x+1<<" "<<y+1<<endl;
}
