#include <bits/stdc++.h>


using namespace std;

int main()
{
   int t,n,a,b;
    double c;
     scanf("%d",&t);
     while(t--)
     {
        scanf("%d",&n);
        double graph[n+1][n+1];
        for(int i=0;i<=n;i++)
          for(int j=0;j<=n;j++)
             graph[i][j]=-1;
        
        cin>>a>>b>>c;
        
        do
        {
            graph[a-1][b-1]=c;
            graph[b-1][a-1]=c;
            cin>>a>>b>>c;
        
        }while(a>0);
 /*
 void floydWarshall() {
       for( int k = 0; k < n; k++ )
       for( int i = 0; i < n; i++ )
       for( int j = 0; j < n; j++ )
           graph[i][j] = min( graph[i][j], graph[i][k] + graph[k][j] );
   }*/


        for (int k = 0;k< n;k++)
        {
            for (int i = 0;i< n;i++)
            { 
                if(i==k)
                    continue;
                for (int j = i+1;j<n;j++)
                {
                    if(j==k)
                        continue; // 
                    graph[j][i]=graph[i][j] = max(graph[i][j], min(graph[i][k],graph[k][j]));
                
                }
         
            }
        }
       
          printf("%.6lf\n",graph[0][n-1]);
    }
 
}
 