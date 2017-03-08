#include<cstdio>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
#include<iostream>
#include<string>
#include<cstring>
#include<climits>
#include<vector>
#define pii pair<int,int>
#define A first
#define B second
#define mp make_pair
#define pb push_back
using namespace std;
int n,a;
map <int,int> M1,M2;
set <int> S;
vector <int> ans;
vector <pii> v;
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&a);
        if(M1.count(a)){
            ans.pb(M1[a]); ans.pb(a); ans.pb(M1[a]); ans.pb(a);
            v.clear();
            M2.clear(); M1.clear(); S.clear();
        }
        else{
            if(M2.count(a)){
                int pos = M2[a];
                while(v.back().B > pos && !v.empty()){
                    M1[v.back().A] = a;
                    v.pop_back();
                }
                v.pop_back();
                if(S.count(a))
                    M1[a] = a;
                S.insert(a);
            }
            M2[a] = i;
            v.pb(pii(a,i));
        }
    }
    printf("%d\n",ans.size());
    for(int i=0;i<ans.size();i++)
        printf("%d ",ans[i]);
    return 0;
}