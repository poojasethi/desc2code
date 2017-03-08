#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cstdio>
#include<map>
using namespace std;
string s;
map<string,vector<int> >M;
map<pair<string,string>,int>N;
string s1,s2;
int ans,len1,len2;
void f(int i,int j)
{
    // cout<<i<<" "<<j<<endl;
    int r = max(i+len1,j+len2);
    int l = min(i,j);
    if(ans==-1||r-l<ans)
        ans=r-l;
}
int main()
{
    int i,j;
    while(cin>>s)
    {
        int len=s.size();
        M.clear();
        N.clear();
        for(i=0; i<len; i++)
        {
            string tmp = "";
            for(j=0; j<4&&i+j<len; j++)
            {
                tmp += s[i+j];
                M[tmp].push_back(i);
            }
        }
        int q;

        scanf("%d",&q);
        while(q--)
        {
            cin>>s1>>s2;
            i=0;
            j=0;
            ans=-1;
            len1=s1.size();
            len2=s2.size();
            vector<int>g(M[s1]);
            vector<int>t(M[s2]);
            if(N[make_pair(s1,s2)])
            {
                printf("%d\n",N[make_pair(s1,s2)]);
                continue;
            }
            if(g.size()==0||t.size()==0)
            {
                N[make_pair(s1,s2)]=-1;
                cout<<-1<<endl;
                continue;
            }

            vector<int>::iterator it1 = g.begin();
            vector<int>::iterator it2 = t.begin();
            while(it1!=g.end()&&it2!=t.end())
            {
                f(*it1,*it2);
                if(*it1<*it2)
                    it1++;
                else
                    it2++;

            }
            printf("%d\n",ans);
            N[make_pair(s1,s2)]=ans;
            N[make_pair(s2,s1)]=ans;
        }
    }
}
