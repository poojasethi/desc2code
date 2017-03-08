#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i,j,k,l,m,n,num[110],tmp[110],c,tc;
    while(cin>>tc)
    {
        for(l=1; l<=tc; l++)
        {
            cin>>n;
            c=0;
            for(i=0; i<n; i++)
            {
                cin>>num[i];
                tmp[i]=num[i];
            }
            sort(num,num+n);
            for(i=0; i<n; i++)
            {
                if(num[i]!=tmp[i])
                {
                    for(j=i+1; j<n; j++)
                    {
                        if(tmp[j]==num[i])
                        {
                            swap(tmp[i],tmp[j]);
                            c++;
                            break;
                        }
                    }
                }
            }
            printf("Case %d: %d\n",l,c);
        }
    }

    return 0;
}
