/**
http://www.codechef.com/OCT13/problems/KMHAMHA
*/

/**
NOTE: This prblem basically requires the bipartite data structure for solving the prbolem.
        We need to build two DIFFERENT VERTEX SET ONE WHICH CONTAINS THE ROW NO AS VERTEX AND
        OTHER ONE WHICH CONTAINS THE COLOUMN AS VETREX. THEN WE WOULD CREATE THE EDGE
        FOR EACH POSITION OF VERTEX I.E. (DEMON).  SINCE FOR KILLING ANY DEMON WE NEED TO
        HIT EITHER IN ROW OR COLOMN SET VERTEX THAT'S WHY WE HAVE CREATED BIPARTITE GRAPH.
        NOW THE PROBLEM IS SIPMULATED VERY SIMILAR TO FINDING THE MINIMUM NO OF VERTEX'S
        WHICH COVERS THE ALL EDGES OF THE GRAPH.I.E. FINDING THE VERTEX COVER OF THE GRAPH.
*/

/**
Input
1
3
0 0
1 0
0 1

Output
2
*/
#include <cstdio>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <map>
#include <cstring>
using namespace  std;
#define N 1005
#define INF 1000000000


vector<int> adj[N];

int match[N];
bool seen[N];

/**
Function for maximum bipartite matching.
*/
bool bmp(int u)
{
    for(int i=0;i<adj[u].size();i++)
    {
        int v=adj[u][i];
        if(seen[v]) continue;
        seen[v]=true;
        if(match[v]==-1 || bmp(match[v])){
            match[v]=u;
            return true;
        }
    }
    return false;
}


int main()
{

    int T;
    for (scanf("%d", &T); T --;)
    {
        int n;
        scanf("%d", &n);
        /**
        Since the value of row and coloumn is in the range of r,c<=10^9.
        And it's ensured that these values would not be more than 1000.(i.e. No. of inputs).
        So we have used here hash for those big values to optimise the grapgh in An adjacency
        matrix properly. But we need to ensure that hash value is returning the same value
        for same value of r and c.
        */

        map<int, int> hashX, hashY;
        for (int i = 0; i < n; ++ i)
        {
            int x, y;
            scanf("%d%d", &x, &y);
            if (!hashX.count(x))
             {
                int newid = hashX.size();
                adj[newid].clear();
                hashX[x] = newid;
            }
            x = hashX[x];
            if (!hashY.count(y))
            {
                int newid = hashY.size();
                hashY[y] = newid;
            }
            y = hashY[y];
            adj[x].push_back(y);
        }

        memset(match, -1, sizeof(match));

        int maxMatch = 0;
        for (int i = 0; i < hashX.size(); ++ i) {
            memset(seen,false,sizeof(seen));
            if (bmp(i)) {
                ++ maxMatch;
            }
        }
        printf("%d\n",maxMatch);
    }

    return 0;
}
