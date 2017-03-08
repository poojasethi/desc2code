#include <bits/stdc++.h>
using namespace std;
int n;
int comp(int index,int a[])
{
    int ans=1,i;
    vector<int>v;
    vector<int>::iterator temp;
    v.push_back(a[index]);
    for(i=index+1;i<index+n;i++)
    {
        if(a[i]<v[0])
            v[0]=a[index];
        else if(a[i]>v[v.size()-1])
        {
            ans++;
            v.push_back(a[i]);
        }

        else
        {
            temp=upper_bound(v.begin(),v.end(),a[i]);
            *temp=a[i];
        }
    }
    return ans;
}
int main()
{
    int i,j,t;
    scanf("%d",&t);
    /*while(t--)
    {
    scanf("%d",&n);
    long long int a[2*n],t[2*n];
    memset(t,0,sizeof(t));
    for(i=0;i<n;i++)
       {
           scanf("%lld",&a[i]);
            a[n+i]=a[i];
            t[i]=1;
           t[n+i]=1;
       }
    for(i=0;i<2*n;i++)
    {
        for(j=0;j<i;j++)
        {
            if(a[i]>a[j])
                t[i]=max(1+t[j],t[i]);
        }
    }

    for(i=0;i<2*n;i++)
        printf("%lld ",t[i]);
    long long int m=t[0];
    for(i=1;i<2*n;i++)
    {
        if(t[i]>m)
        m=t[i];
    }
    printf("%lld\n",m);
    }*/
    while(t--)
    {
        scanf("%d",&n);
        int a[2*n],l=0;
        vector<pair<int,int> >c(n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            a[i+n]=a[i];
            c[i].first=a[i];
            c[i].second=i;
        }
        sort(c.begin(),c.end());
        for(i=0;i<min(37,n);i++)
        {
            l=max(l,comp(c[i].second,a));
        }
        printf("%d\n",l);
    }
    return 0;
}
