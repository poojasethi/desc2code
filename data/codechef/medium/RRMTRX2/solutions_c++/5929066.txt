#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
using namespace std;
int mod=10000007;
map<int,int> L;
vector<vector<int> > M;int n,m;
int cou(int s)
{
    if(s==m)return 1;
	if(L.find(s)!=L.end())return L[s];
    int c=0;
    for(int i=0;i<n;i++)
    {
        c=c+(M[i][s]*cou(s+1));
        c%=mod;
    }
L[s]=c;
    return c;
}
int main()
{

    scanf("%d",&n);
    scanf("%d",&m);
    M=vector<vector<int> > ( n,vector<int> (m,0) );

    for(int i=0;i<n;i++)
    for(int j=0;j<m;j++)
    scanf("%d",&M[i][j]);

    printf("%d\n",(cou(0)+mod)%mod);

}
