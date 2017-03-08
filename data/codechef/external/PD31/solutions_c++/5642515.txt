/*
	Author   : Sandeep Ravindra
	Contest  : Practice
	Problem  : Is it a tree
*/

#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<vector>
#include<limits.h>
#include<list>

using namespace std;

#define	    ll		    long long int
#define     D               double
#define     LD              long double

#define     s(n)	    scanf("%d",&n)
#define     ss(n)	    scanf("%s",n)
#define     sc(n)	    scanf("%c",&n)
#define     sl(n)	    scanf("%ld",&n)
#define     sll(n)	    scanf("%lld",&n)

#define     fr(i,a,b)	    for(int i=a;i<b;i++)

#define     max(a,b)	    ((a)>(b)?(a):(b))
#define     min(a,b)	    ((a)<(b)?(a):(b))

#define	    p(n)	    printf("%d",n)
#define	    pl(n)	    printf("%ld",n)
#define	    pll(n)	    printf("%lld",n)
#define	    pbl(n)	    printf("\n")

#define     MP              make_pair
#define     vi              vector<int>
#define     PB              push_back
#define     S               second
#define     F               first

#define     TEST            int _t; s(_t); while(_t--)

typedef     pair<int,int> pii;

vector<vector<int> > tree;
vector<bool> visited;
bool ans;
int c=0;

void dfs(int x)
{
    c=0;
    for(vector<int>::iterator it = tree[x].begin(); it != tree[x].end(); it++)
    {
        if(visited[*it] == true)
            c++;
    }

    if(c>1)
        ans = false;

    for(vector<int>::iterator it = tree[x].begin(); it != tree[x].end(); it++)
    {
        if(visited[*it] == false)
        {
            visited[*it] = true;
            dfs(*it);
        }
    }
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("in.txt","r",stdin);
	#endif
    int n,m;
    s(n),s(m);
    ans = true;
        tree = vector<vector<int> > (n);
        fr(i,0,m)
        {
            int u,v;
            s(u),s(v);
            u--,v--;
            tree[u].PB(v);
            tree[v].PB(u);
        }
        visited = vector<bool> (n,false);
        visited[0] = true;
        dfs(0);
        for(int i=0;i<n;i++)
            if(visited[i] == false)
                ans = false;
        if(n != m+1)
            ans = false;

        if(ans == true)
            printf("YES\n");
        else
            printf("NO\n");
return 0;
}
