// not my code

#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int on[50005], f[50005], fo[50005];
vector<int> fl[50005];

int main()
{
    //freopen ("coba.txt","r",stdin);
    int n, m, q; scanf("%d%d%d", &n, &m, &q);
    int k; scanf("%d", &k);
    for(int i=0;i<k;i++) { int x; scanf("%d", &x); on[x]=1; }
    for(int i=0;i<m;i++)
    {
       int a, b; scanf("%d%d", &a, &b);
       if(f[a]>f[b]) swap(a,b);
       f[a]++; fl[a].push_back(b);
       fo[b]+=on[a];
    }

    while(q--)
    {
       char in[3]; scanf("%s", in);
       int a, b;
       if(in[0]=='O')
       {
          scanf("%d", &a); on[a]=1;
          for(int i=0;i<fl[a].size();i++) fo[fl[a][i]]++;
       }
       else if(in[0]=='F')
       {
          scanf("%d", &a); on[a]=0;
          for(int i=0;i<fl[a].size();i++) fo[fl[a][i]]--;
       }
       else if(in[0]=='A')
       {
          scanf("%d%d", &a,  &b);
          if(f[a]>f[b]) swap(a,b);
          f[a]++; fl[a].push_back(b);
          fo[b]+=on[a];
       }
       else if(in[0]=='D')
       {
           int id=-1; scanf("%d%d", &a, &b);
           for(int i=0;i<fl[a].size();i++) if(fl[a][i]==b) id=i;
           if(id==-1)
           {
              swap(a,b);
              for(int i=0;i<fl[a].size();i++) if(fl[a][i]==b) id=i;
           }
           if(on[a]) fo[b]--; f[a]--;
           fl[a][id]=fl[a][fl[a].size()-1]; fl[a].pop_back();
       }
       else
       {
          scanf("%d", &a);
          int ans=fo[a];
          for(int i=0;i<fl[a].size();i++) ans+=on[fl[a][i]];
          printf("%d\n", ans);
       }
    }
    return 0;
}