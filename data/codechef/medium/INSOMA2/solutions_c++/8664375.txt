#include<bits/stdc++.h>
#define mp make_pair
using namespace std;

map < pair < pair < long long, long long > , long long > , long long > w;
string s;
int n;
char a[1002][1002];

long long cont(int pos, int x, int y)
{
    if(x==0||y==0||y>n||x>n)return 0;
    if(w.find(mp(mp(x,y),pos))!=w.end()) return w[mp(mp(x,y),pos)];
    if(a[x][y]==s[pos]&&s[pos+1]=='\0')return 1;
    if(a[x][y]=='X')return 0;
    if(a[x][y]!=s[pos])return 0;

    long long int c=0;
    c += cont(pos+1,x+1,y+1);
    c += cont(pos+1,x-1,y+1);
    c += cont(pos+1,x-1,y-1);
    c += cont(pos+1,x+1,y-1);

    w[mp(mp(x,y),pos)] = c;
    return c;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t,i,j;
    long long int r=0;
        cin>>n;

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                cin>>a[i][j];
            }
        }

        for(i=0;i<=n;i++)
        {
            a[i][0]='X';
            a[0][i]='X';
        }

        cin>>s;

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(s[0]==a[i][j])
                {
                    r += cont(0,i,j);
                }
            }
        }
        cout<<r<<endl;
    return 0;
}

