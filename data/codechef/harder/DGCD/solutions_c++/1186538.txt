#include<stdio.h>
#include<string.h>
int e[210000][6],edge[110000][7],v[110000][6],size[110000],dfsq[220000],t[1000000][3]
    ,tr[110000][3],t1[1000000][3],tr1[110000][3],lev[110000],link[110000],link1[110000]
    ,lca[20][110000],first[110000];
char s[200];
int n,tot,etot,ttot,tot1,ttot1;

int rmq(int o,int p)
{
    if (o>p) {int q=o;o=p;p=q;}
    int k=0,j=1;
    while (j*2<=p-o+1) {j*=2;k++;}
    return lev[lca[k][o]]<lev[lca[k][p-j+1]]?lca[k][o]:lca[k][p-j+1];
}

int gcd(int o,int p)
{
    o=o<0?-o:o;
    p=p<0?-p:p;
    if (o<p) {int q=o;o=p;p=q;}
    return p==0?o:gcd(p,o%p);
}

int max(int o,int p) {return o>p?o:p;}

void work_l(int o,int p)
{
    bool bq=false;
    while (v[o][1]>=0)
    {
        int j=v[o][1];
        v[o][4]=p;
        link[++link[0]]=o;
        link1[link[0]]=v[link[link[0]]][3]-v[link[link[0]-1]][3];
        if (!bq) {link1[link[0]]+=v[link[link[0]-1]][3];bq=true;}
        v[o][5]=link[0];
        o=e[j][0];
    }
    v[o][4]=p;
    link[++link[0]]=o;
    v[o][5]=link[0];
    link1[link[0]]=v[link[link[0]]][3]-v[link[link[0]-1]][3];
}

void build(int o,int l,int r)
{
    if (l==r) {return;}
    t[o][2]=0;
    int mid=(l+r)/2;

    if (t[o][0]==0)
    {
        tot++;
        t[o][0]=tot;
        t[tot][0]=t[tot][1]=t[tot][2]=0;
    }
    build(t[o][0],l,mid);

    if (t[o][1]==0)
    {
        tot++;
        t[o][1]=tot;
        t[tot][0]=t[tot][1]=t[tot][2]=0;
    }
    build(t[o][1],mid+1,r);
}


void build1(int o,int l,int r)
{
    if (l==r) {t1[o][2]=link1[l];return;}
    int mid=(l+r)/2;

    if (t1[o][0]==0)
    {
        tot1++;
        t1[o][0]=tot1;
        t1[tot1][0]=t1[tot1][1]=t1[tot1][2]=0;
    }
    build1(t1[o][0],l,mid);

    if (t1[o][1]==0)
    {
        tot1++;
        t1[o][1]=tot1;
        t1[tot1][0]=t1[tot1][1]=t1[tot1][2]=0;
    }
    build1(t1[o][1],mid+1,r);
    t1[o][2]=gcd(t1[t1[o][0]][2],t1[t1[o][1]][2]);
}

void dfs(int o,int fa,int ol)
{
    dfsq[++dfsq[0]]=o;
    first[o]=dfsq[0];
    lev[o]=ol;
    int j=v[o][0],bn=-1;
    size[o]=1;
    while (j!=0)
    {
        if (e[j][0]!=fa)
        {
            dfs(e[j][0],o,ol+1);
            dfsq[++dfsq[0]]=o;
            size[o]+=size[e[j][0]];
            if ((bn<0)||(size[e[j][0]]>size[bn])) {bn=e[j][0];}
        } else v[o][2]=j;
        j=e[j][3];
    }

    if (bn==-1) {v[o][1]=-1;}
    else
    {
        j=v[o][0];
        while (j!=0)
        {
            if (e[j][0]!=fa)
              if (e[j][0]!=bn)
                {
                    if (v[e[j][0]][1]!=-1)
                    {
                      int l=link[0]+1;
                      work_l(e[j][0],ttot);
                      int r=link[0];

                      tot++;
                      tr[ttot][0]=tot;
                      tr[ttot][1]=l;
                      tr[ttot][2]=r;
                      t[tot][0]=t[tot][1]=t[tot][2]=0;
                      build(tr[ttot][0],l,r);

                      tot1++;
                      tr1[ttot][0]=tot1;
                      tr1[ttot][1]=l+1;
                      tr1[ttot][2]=r;
                      t1[tot1][0]=t1[tot1][1]=t1[tot1][2]=0;
                      build1(tr1[ttot][0],l+1,r);
                      ttot++;
                    }
                }
               else
               {
                   v[o][1]=j;
                   edge[e[j][2]][3]=1;
               }
            j=e[j][3];
        }
    }
    if (o==0)
    {
        int l=link[0]+1;
        work_l(o,ttot);
        int r=link[0];
        tot++;
        tr[ttot][0]=tot;
        tr[ttot][1]=l;
        tr[ttot][2]=r;
        t[tot][0]=t[tot][1]=t[tot][2]=0;
        build(tr[ttot][0],l,r);

        if (v[0][1]!=-1) {
        tot1++;
        tr1[ttot][0]=tot1;
        tr1[ttot][1]=l+1;
        tr1[ttot][2]=r;
        t1[tot1][0]=t1[tot1][1]=t1[tot1][2]=0;
        build1(tr1[ttot][0],l+1,r);
        }
        ttot++;
    }
}

void change(int o,int l,int r,int p,int c)
{
    if (l==r) {link1[l]+=c;t1[o][2]=link1[l];return;}
    int mid=(l+r)/2;
    if (p<=mid) change(t1[o][0],l,mid,p,c);
    else change(t1[o][1],mid+1,r,p,c);
    t1[o][2]=gcd(t1[t1[o][0]][2],t1[t1[o][1]][2]);
}

void add(int o,int l,int r,int p,int q,int c)
{
    if ((p<=l)&&(r<=q)) {t[o][2]+=c;return;}
    int mid=(l+r)/2;
    if (p<=mid) add(t[o][0],l,mid,p,q,c);
    if (mid<q) add(t[o][1],mid+1,r,p,q,c);
}

void add_v(int o,int p,int c)
{
    if (o==p)
    {
        v[o][3]+=c;
        if (v[o][4]!=-1)
        {
            if (lev[o]-lev[link[tr[v[o][4]][1]]]+tr[v[o][4]][1]<tr[v[o][4]][2])
               change(tr1[v[o][4]][0],tr1[v[o][4]][1],tr1[v[o][4]][2]
                     ,lev[o]-lev[link[tr[v[o][4]][1]]]+tr[v[o][4]][1]+1,-c);

            if (lev[link[tr[v[o][4]][1]+1]]<=lev[link[v[p][5]]])
               change(tr1[v[o][4]][0],tr1[v[o][4]][1],tr1[v[o][4]][2]
                     ,v[p][5],c);
        }
        return;
    }
    if ((edge[e[v[o][2]][2]][3]==-1)&&(v[o][1]<0))
    {
        v[o][3]+=c;
        add_v(e[v[o][2]][0],p,c);
        return;
    }

    int l=tr[v[o][4]][1],r=tr[v[o][4]][2];
    if (lev[o]-lev[link[tr[v[o][4]][1]]]+tr[v[o][4]][1]<tr[v[o][4]][2])
       {change(tr1[v[o][4]][0],tr1[v[o][4]][1],tr1[v[o][4]][2]
             ,lev[o]-lev[link[tr[v[o][4]][1]]]+tr[v[o][4]][1]+1,-c);
             r=lev[o]-lev[link[tr[v[o][4]][1]]]+tr[v[o][4]][1];}
    if (lev[link[tr[v[o][4]][1]+1]]<=lev[link[v[p][5]]])
       {change(tr1[v[o][4]][0],tr1[v[o][4]][1],tr1[v[o][4]][2]
             ,v[p][5],c);l=v[p][5];}
    add(tr[v[o][4]][0],tr[v[o][4]][1],tr[v[o][4]][2],l,r,c);
    if (lev[link[tr[v[o][4]][1]]]>lev[p]) add_v(e[v[link[tr[v[o][4]][1]]][2]][0],p,c);
}

int find(int o,int l,int r,int p)
{
    if (l==r) return v[link[l]][3]+t[o][2];
    int ans=t[o][2],mid=(l+r)/2;
    if (p<=mid) ans+=find(t[o][0],l,mid,p);
    if (mid<p) ans+=find(t[o][1],mid+1,r,p);
    return ans;
}

int find1(int o,int l,int r,int p,int q)
{
    if ((p<=l)&&(r<=q)) return t1[o][2];
    int u=0,v=0,mid=(l+r)/2;
    if (p<=mid) u=find1(t1[o][0],l,mid,p,q);
    if (mid<q) v=find1(t1[o][1],mid+1,r,p,q);
    return gcd(u,v);
}

int find_gcd(int o,int p)
{
    //if (v[o][2]==-1) {return v[o][3];}
    if (lev[o]<lev[p]) return 0;
    if (o==p)
    {
        if ((edge[e[v[o][2]][2]][3]==-1)&&(v[o][1]<0)) return v[o][3];
        return find(tr[v[o][4]][0],tr[v[o][4]][1],tr[v[o][4]][2],lev[o]-lev[link[tr[v[o][4]][1]]]+tr[v[o][4]][1]);
    }
    if (edge[e[v[o][2]][2]][3]==-1)
    {
        int tmp=v[o][3];
        if (v[o][1]>=0) tmp=find(tr[v[o][4]][0],tr[v[o][4]][1],tr[v[o][4]][2],v[o][5]);
        return gcd(tmp,find_gcd(e[v[o][2]][0],p));
    }
    int l=tr[v[o][4]][1]+1,r=v[o][5];
    if (lev[link[l]]<=lev[p]) l=v[p][5]+1;
    if (lev[link[r]]>=lev[link[tr1[v[o][4]][2]]]) r=tr1[v[o][4]][2];
    return gcd(find1(tr1[v[o][4]][0],tr1[v[o][4]][1],tr1[v[o][4]][2],l,r),find_gcd(e[v[link[l]][2]][0],p));
}

int main()
{
    //freopen("1.txt","r",stdin);
    //freopen("2(1).txt","w",stdout);
    scanf("%d",&n);
    for (int i=0;i<n;i++) {v[i][0]=0;v[i][1]=first[i]=v[i][5]=v[i][4]=-1;}
    tot=ttot=etot=tot1=ttot1=0;
    link[0]=link1[0]=0;
    v[0][2]=-1;e[0][0]=-1;
    for (int i=1;i<n;i++)
    {
        first[i]=-1;
        scanf("%d%d",&edge[i][0],&edge[i][1]);
        edge[i][3]=-1;
        etot++;
        e[etot][0]=edge[i][1];
        e[etot][2]=i;
        e[etot][3]=v[edge[i][0]][0];
        v[edge[i][0]][0]=etot;
        edge[i][5]=etot;
        e[etot][5]=-1;

        etot++;
        e[etot][0]=edge[i][0];
        e[etot][2]=i;
        e[etot][3]=v[edge[i][1]][0];
        v[edge[i][1]][0]=etot;
        edge[i][6]=etot;
        e[etot][5]=-1;
    }
    for (int i=0;i<n;i++) scanf("%d",&v[i][3]);
    dfsq[0]=0;
    dfs(0,0,1);

    for (int i=0;i<=dfsq[0];i++) lca[0][i]=dfsq[i];
    int j=1,k=0;
    while (lca[k][0]>=1+j)
    {
        k++;
        lca[k][0]=0;
        for (int i=1;i+j<=lca[k-1][0];i++)
            lca[k][++lca[k][0]]=lev[lca[k-1][i]]<lev[lca[k-1][i+j]] ? lca[k-1][i] : lca[k-1][i+j];
        j*=2;
    }

    int q=0;scanf("%d",&q);
    scanf("%s",&s);
    while (q>0)
    {
        q--;
        if (s[0]=='C')
        {
            int x,y,val;
            scanf("%d%d%d",&x,&y,&val);
            if (val!=0) {
            int fa=rmq(first[x],first[y]);
            add_v(x,fa,val);
            add_v(y,fa,val);
            //add_v(fa,e[v[fa][2]][0],val);
            add_v(fa,fa,-val);}
        } else
        {
            int x,y;
            scanf("%d%d",&x,&y);
            int fa=rmq(first[x],first[y]);
            printf("%d\n",gcd(find_gcd(x,fa),find_gcd(y,fa)));
        }
        if (q!=0) scanf("%s",&s);
    }

    return 0;
}
