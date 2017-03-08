#include<bits/stdc++.h>
using namespace std;
string s;
int used[19][19][1009];
int m;
int ans[1009],l;
void rec(int x,int y,int z)
{
    int i;
    used[x][y][z]=1;
    if(z==m+1){l=1;return;}
    for(i=x+1;i<=10;i++)
    {
        if(i!=y&&s[i-1]=='1'&&used[i-x][i][z+1]==0)
        {
            ans[z]=i;
            rec(i-x,i,z+1);
            if(l)return;
        }
    }
}
int main()
{
    cin>>s;
    cin>>m;
    int i;
    rec(0,0,1);
    if(l==0){cout<<"NO"<<endl;return 0;}
    cout<<"YES"<<endl;
    for(int i=1;i<=m;i++)cout<<ans[i]<<" ";
    cout<<endl;
}


