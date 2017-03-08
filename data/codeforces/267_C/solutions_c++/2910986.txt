#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <math.h>
#define N 110
#define K 5100
using namespace std;
long double m[N][N], x[N];
int a[N][N], u[N], y[N], s[K], e[K];
vector <int> v[N], d[N];
void dfs(int i)
{
    int j;
    u[i]=1;
    for(j=0; j<v[i].size(); a[i][v[i][j]]++, a[i][i]--, j++)
        if(!u[v[i][j]]) dfs(v[i][j]);
}
int main()
{
    int n, k, i, j, t, l;
    long double b, z;
    for(scanf("%d%d", &n, &l), k=0; k<l; k++)
    {
        scanf("%d%d%d", &i, &j, &t);
        i--;
        j--;
        s[k]=i;
        e[k]=j;
        v[i].push_back(j);
        v[j].push_back(i);
        d[i].push_back(t);
        d[j].push_back(t);
    }
    dfs(0); a[0][0]--;
    for(i=0; i<n-1; m[i][j]=-a[i][0], i++)
        for(j=0; j<n-1; m[i][j]=a[i][j+1], j++);
    for(i=0; i<n-1; i++)
    {
        if(!u[i]) continue;
        for(j=0, t=0; t<n-1; j=fabs(m[i][t])>fabs(m[i][j])?t:j, t++);
        if(fabs(m[i][j])<1E-9) break;
        y[i]=j;
        for(k=0; k<n-1; k++)
            if(k!=i)
                for(z=m[k][j]/m[i][j], t=0; t<n; m[k][t]-=m[i][t]*z, t++);
        
    }
    if(i<n-1)
    { 
        for(printf("0.0\n"), i=0; i<l; printf("0.0\n"), i++);
        return 0;
    }
    for(x[0]=1, i=0; i<n-1; i++)
        if(u[i]) x[y[i]+1]=m[i][n-1]/m[i][y[i]];
    for(b=1E20, i=0; i<n; i++)
        if(u[i])
            for(j=0; j<v[i].size(); j++)
            {
                z=fabs(x[v[i][j]]-x[i]);
                if(z>1E-9 && d[i][j]/z<b) b=d[i][j]/z;
            }
    printf("%.13lf\n", (double)b);
    for(i=0; i<l; printf("%.13lf\n", (double)((x[e[i]]-x[s[i]])*b)), i++);
    return 0;
}