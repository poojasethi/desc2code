#include<bits/stdc++.h>

using namespace std;

map<int,int> is,js;
int isz[4020],jsz[4020],r,c,g[4020][4020];
vector< pair< pair<int,int>,pair<int,int> > > segs;
int di[]={1,0,-1,0};
int dj[]={0,-1,0,1};
char d[]="DLUR";

int compress(map<int,int> &m,int s[]){
    int last=m.begin()->first-1;
    int next=1;
    for(map<int,int>::iterator it=m.begin();it!=m.end();it++){
        int cur=it->first;
        if(last+1!=cur)
            s[next++]=cur-last-1;
        s[next]=1;
        it->second=next++;
        last=cur;
    }
    return next+1;
}

void FF(int i,int j){
    if(i<0 || j<0 || i==r || j==c || g[i][j])
        return;
    g[i][j]=2;
    for(int k=0;k<4;k++)
        FF(i+di[k],j+dj[k]);
    return;
}

int main(){
    int i=0,j=0,n;
    scanf("%d",&n);
    while(n--){
        char c;
        int s;
        scanf(" %c%d",&c,&s);
        int k=find(d,d+4,c)-d;
        int ii=i+s*di[k];
        int jj=j+s*dj[k];
        is[i],is[ii],js[j],js[jj];
        segs.push_back(make_pair(make_pair(i,j),make_pair(ii,jj)));
        i=ii;
        j=jj;
    }
    r=compress(is,isz);
    c=compress(js,jsz);
    for(int k=0;k<segs.size();k++){
        int si=is[segs[k].first.first];
        int sj=js[segs[k].first.second];
        int ei=is[segs[k].second.first];
        int ej=js[segs[k].second.second];
        for(i=min(si,ei);i<=max(si,ei);i++)
            for(j=min(sj,ej);j<=max(sj,ej);j++)
                g[i][j]=1;
    }
    FF(0,0);
    long long ans=0;
    for(i=0;i<r;i++)
        for(j=0;j<c;j++)
            if(g[i][j]!=2)
                ans+=isz[i]*1ll*jsz[j];
    printf("%I64d\n",ans);
    return 0;
}
