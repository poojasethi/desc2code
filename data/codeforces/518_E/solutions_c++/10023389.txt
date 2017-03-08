#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <math.h>
using namespace std;
#define INF  0x3fffffff
char s[2];
int a[200000];

int main()
{
    int n,k;
    cin>>n>>k;
    for(int i=0;i<n;i++)
    {
        scanf("%s",s);
        if(s[0]=='?')
            a[i]=INF;
        else
            sscanf(s,"%d",&a[i]);
    }
    for(int i=n;i<n+k;i++)
        a[i]=INF+1;
    for(int i=0;i<k;i++)
    {
        int mi=-INF,cnt=0;
        for(int j=i;j<n+k;j+=k)
        {
            if(a[j]==INF)
                cnt++;
            else
            {
                if(a[j]-mi<=cnt)
                {
                    cout<<"Incorrect sequence";
                    return 0;
                }
                int num=max(mi+1, min(a[j]-cnt,-cnt/2));
                for(int tmp=cnt;tmp>0;tmp--)
                {
                    int idx=j-tmp*k;
                    a[idx]=num++;
                }
                mi=a[j];
                cnt=0;
            }
        }
    }
    for(int i=0;i<n;i++)
	{
		if(i==n-1) cout<<a[i];
		else cout<<a[i]<<" ";
	}
	return 0;
}
