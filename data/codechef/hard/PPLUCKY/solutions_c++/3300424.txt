/**
LINK:::http://www.codechef.com/COOK39/problems/PPLUCKY
*/
/**
INPUT:
  3
  4
  4747
  10
  4447477747
  8
  44474777
OUTPUT:
4
20
11

*/

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <stack>
#define MOD 100005
#define N 100005
using namespace std;

char str[N];
int tree[N];
typedef vector<int> vi;
typedef long long  LL;

/**
NOTE: Below algorithm will work well in the situation when as soon as we are getting the
      '4' and '7' we are earsing them and after erasing them we are considering the
      current index postion of them add adding them to the result value.
*/

/**

//code related to BIT.
int read(int idx)
{
    int sum=0;
    while(idx>0)
    {
        sum+=treeIdx[idx];
        idx-=idx&(-idx);
    }
    return sum;
}
void update(int idx,int max,int val)
{
    int i;
    while(idx<max)
    {
        treeIdx[idx]+=val;
        idx+=idx&(-idx);
    }
}

void solve1()
{
int i,j,k,t,n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        scanf("%s",s);
        //reset the treeIdx tree.
        for(i=0;i<n;i++)
        {
            treeIdx[i]=0;
        }
        //update the value of the tree.
        for(i=0;i<n;i++)
          update(i+1,n+1,1);

        //Now take the stack and tree for keeping track
        //of erased index of the string.
        stack<int> st;
        set<int> indexSet;
        set<int>::iterator itr;
        for(i=0;i<n;i++)
         indexSet.insert(i+1);

        //Now traverse the stack and try to match the '4' ans '7'
        //that will be erased
        int ans=0;
        for(i=0;i<n;i++)
        {
            if(s[i]=='4')
            st.push(i);
            else if(s[i]=='7')
            {
                if(!st.empty())
                {
                    j=st.top();
                    st.pop();
                    //now calcualte ans add the index of '4' and '7' to ans.
                    ans+=read(j+1);

                    //erase those values from the set.
                    indexSet.erase(i+1);
                    indexSet.erase(j+1);

                    //Also set the index position in the IndexTree after erasing
                    //those index from the IndexTree.
                    update(i+1,n+1,-1);
                    update(j+1,n+1,-1);

                }
            }
        }
        printf("\nAns:%d\n",ans);
    }
}
*/

/**
NOTE: Method 2 for actual solution according to the problem.
*/
int read(int idx)
{
	int sum = 0;
	while (idx > 0) sum =(sum+tree[idx]), idx -= (idx & -idx);
	return sum;
}

void update(int idx ,int maxn,int val)
{
	while (idx <= maxn) tree[idx]=(tree[idx]+val), idx += (idx & -idx);
}

void solve2()
{
    int i,j,k,T,n,totl=0;
   scanf("%d",&T);

   while(T--)
   {
      scanf("%d",&n);
      totl+=n;
      scanf("%s",str);

      set<int> S;
      //reset the tree[] array.
      for(i=0;i<=n;i++)
        tree[i]=0;

      vi now;

      for(i=1;i<=n;i++)
      {
         update(i,n+1,+1);
         S.insert(i);
      }

      for(i=0;i<n;i++)
      {
         if(str[i]=='4' && str[i+1]=='7')
            now.push_back(i+1);
      }

      LL ans=0;

      while(!now.empty())
      {
         vi tmp; // The new positions for P
         vi del; // The indexes with '7' which get deleted

         for(i=0;i<now.size();i++)
         {
            int x=read(now[i]);
            ans+=x;

            S.erase(S.find(now[i]));
            set<int>::iterator it=S.upper_bound(now[i]);
            del.push_back( *it);
            S.erase(S.find(*it));

            if(S.empty()) continue;

            it=S.lower_bound(now[i]);

            if(it!=S.end() && it!=S.begin() && str[*it-1]=='7')
            {
               --it;
               if(str[*it-1]=='4') tmp.push_back(*it);
            }
         }

         for(i=0;i<now.size();i++)
         {
            update(now[i],n+1,-1);
            update(del[i],n+1,-1);

         }
         now=tmp;
      }
      cout<<ans<<endl;
   }

}

int main()
{
    //solve1();
    solve2();

    return 0;
}
