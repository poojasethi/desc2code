#include<cstdio>
#include<vector>
#include<algorithm>
#include<utility>
#define sf scanf
#define pf printf
#define fr freopen
#define ps for(;;)
#define pb push_back
#define mp make_pair
#define lp(i,a,b) for(int i=a;i<=b;++i)
#define rp(i,a,b) for(int i=a;i>=b;--i)
#define vp(i,v) for(int i=0;i<v.size();++i)
#define wp(i,v) for(int i=int(v.size()-1);i>=0;--i)
using namespace std;
typedef long long ll;
#include<string>
#include<iostream>
namespace sam{
    const int N=1200010,M=26;
    int tr[N][M],pr[N],ln[N],nw=1;
    int add(int c,int lst){
        if(tr[lst][c]){
            int p=lst,q=tr[lst][c];
            if(ln[q]==ln[p]+1)return q;
            else{
                int np=++nw;ln[np]=ln[p]+1;pr[np]=pr[q];
                copy(tr[q],tr[q]+M,tr[np]);pr[q]=np;
                for(;p&&tr[p][c]==q;p=pr[p])tr[p][c]=np;
                return np;
            }
        }else{
            int p=lst,np=++nw;ln[np]=ln[p]+1;
            for(;p&&!tr[p][c];p=pr[p])tr[p][c]=np;
            if(!p)pr[np]=1;
            else{
                int q=tr[p][c];
                if(ln[p]+1==ln[q])pr[np]=q;
                else{
                    int nq=++nw;ln[nq]=ln[p]+1;pr[nq]=pr[q];
                    copy(tr[q],tr[q]+M,tr[nq]);
                    pr[q]=pr[np]=nq;
                    for(;p&&tr[p][c]==q;p=pr[p])tr[p][c]=nq;
                }
            }
            return np;
        }
    }
}
int cnt[1200010][11];
using namespace sam;
int lft[11],rght[11],n;char tmp[50010];
bool cmp(int x,int y){
    return ln[x]>ln[y];
}
int main(){
    sf("%s",tmp+1);
    for(int u=1,i=1;tmp[i];++i){
        u=add(tmp[i]-'a',u);
        ++cnt[u][0];
    }
    sf("%d",&n);
    lp(i,1,n){
        sf("%s%d%d",tmp+1,&lft[i],&rght[i]);
        for(int u=1,j=1;tmp[j];++j){
            u=add(tmp[j]-'a',u);
            ++cnt[u][i];
        }
    }
    //print(1,"");return 0;
    static int tmp[600010*2];
    lp(i,1,nw)tmp[i]=i;
    sort(tmp+1,tmp+nw+1,cmp);
    lp(i,1,nw){
        int u=tmp[i];
        lp(j,0,n)cnt[pr[u]][j]+=cnt[u][j];
    }
    ll ans=0;
    lp(i,1,nw){
        int flg=1;
        lp(j,1,n)if(cnt[i][j]>=lft[j]&&cnt[i][j]<=rght[j]){
        }else flg=0;
        if(flg&&cnt[i][0])ans+=ln[i]-ln[pr[i]];
    }
    pf("%I64d\n",ans);
    //ps;
    return 0;
}