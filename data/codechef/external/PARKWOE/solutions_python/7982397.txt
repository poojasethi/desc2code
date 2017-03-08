#include<bits/stdc++.h>
 
using namespace std;

int up=0,down=0,ans=0,ans1=0;
const int EMPTY = 2147483647;
 
int main()
{
    long long int t;
    
    scanf("%lld",&t);
    for(int io=0;io<t;io++)
    {
            long long int n,m;
            scanf("%lld%lld",&m,&n);
            long long int a[m][n];
             for(int i=0;i<m;i++)
            {
                    for(int j=0;j<n;j++)
                    {
                           a[i][j]=0;
                    }
                    }
            for(int i=0;i<m;i++)
                {
                        for(int j=0;j<n;j++)
                        {
                                scanf("%lld",&a[i][j]);
                    }
                    }
                               up=0;
                               down=0;
                               ans=0;
                               ans1=0;
                        while(a[up][down]!=EMPTY)
                    {
                              long long int laa=EMPTY,lo=EMPTY;
                              if( up+1 < m )
                              {
                                        laa=a[up+1][down];
                                  }                      
                           if(down+1<n)
                           {
                                            lo=a[up][down+1];
                           }                      
                        if(laa>lo)
                        {
                                       ans++;                         
                                       down++;
                         }          
                              else if(lo>laa)
                              {
                                  ans1++;
                                  up++;
                                  }
                                  else if((laa  == EMPTY)  &&  (lo  ==  EMPTY))
                                            a[ up ] [ down ] =EMPTY;
                    }
                    ans=ans+ans1;
                                        cout<<ans<<"\n";
              
                    
   }
    return 0;
    
}