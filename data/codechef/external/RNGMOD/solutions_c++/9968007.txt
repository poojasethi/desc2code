/**************************************
 *        BISMILLAHIR RAHMANIR RAHIM  *
 *           MD: EMRUZ HOSSAIN        *
 *              CUET-CSE-12           *
 **************************************/
 #include<bits/stdc++.h>
 using namespace std;
 typedef long long ll;

#define     mem(x,y)   memset(x,y,sizeof(x))
#define     PB(x)      push_back(x)
#define     POB()      pop_back()
#define     SZ(a)      a.size()
#define     len(a)     strlen(a)
#define     SQR(a)     (a*a)
#define     all(v)     v.begin(),v.end()
#define     fr(i,a,b)  for(i=a;i<=b;i++)
#define     rfr(i,a,b) for(i=a;i>=b;i--)
#define     sf  scanf
#define     pf  printf
#define     mkp make_pair
#define     fs  first
#define     sd  second

#define     getx() getchar()
//#define     getx() getchar_unlocked()

#define     inf  1<<25
#define     sz   20002
#define     eps  1e-9
#define     mod  1000000007
#define     PI   2.0*acos(0.0)


 /*****************************Code start from here**************************/
int A[1000005],prefix_sum[1000005],block,lower_active_bound_of[1000005],upper_active_bound_of[1000005];
vector<int>indexes_of[1000005];
int tree[8*1000005],k,ans[1000005];
struct st
{
    int l,r,id;
}queries[1000005];
bool cmp(st a,st b)
{
    if(a.l/block!=b.l/block)
       return a.l/block<b.l/block;
    return a.r<b.r;
}
void update(int rt,int beg,int endd,int idx,int val)
{
    if(beg==endd)
    {
        tree[rt]=val;
        return;
    }
    int mid=(beg+endd)/2;
    if(idx<=mid)
        update(2*rt,beg,mid,idx,val);
    else
        update(2*rt+1,mid+1,endd,idx,val);
    tree[rt]=max(tree[2*rt],tree[2*rt+1]);
}
void Add(int val,int dirrection)
{
    if(dirrection==1)
    {
        upper_active_bound_of[val]++;
        if(lower_active_bound_of[val]==-1)
            lower_active_bound_of[val]++;
    }
    else
    {
        lower_active_bound_of[val]--;
    }
    if(lower_active_bound_of[val]>upper_active_bound_of[val])
        return;
    update(1,0,1000001,val,indexes_of[val][upper_active_bound_of[val]]-indexes_of[val][lower_active_bound_of[val]]);
}
void Remove(int val,int dirrection)
{
    if(lower_active_bound_of[val]>upper_active_bound_of[val])
        return;
    if(dirrection==0)
    {
        lower_active_bound_of[val]++;
    }
    else
    {
        upper_active_bound_of[val]--;
    }
    if(lower_active_bound_of[val]>upper_active_bound_of[val])
        return;
    update(1,0,1000001,val,indexes_of[val][upper_active_bound_of[val]]-indexes_of[val][lower_active_bound_of[val]]);
}
int main()
{
    //    freopen("output.txt","w",stdout);
    //    freopen("xinput.txt","r",stdin);
   //ios_base::sync_with_stdio(false);
   int a,b,c,d,h,m,n,p,x,y,i,j,q,t,cnt,sm,tmp,curL,curR,L,R;
   sf("%d %d %d",&n,&m,&k);
   block=250;
   for(i=1;i<=n;i++)
   {
       sf("%d",&A[i]);
   }
   prefix_sum[0]=0;
   indexes_of[0].push_back(0);
   for(i=1;i<=n;i++)
   {
       prefix_sum[i]=(prefix_sum[i-1]+A[i])%k;
       indexes_of[prefix_sum[i]].push_back(i);
   }
   for(i=0;i<m;i++)
   {
       sf("%d %d",&queries[i].l,&queries[i].r);
       queries[i].id=i;
       queries[i].l--;
   }
   sort(queries,queries+m,cmp);
   for(i=0;i<1000005;i++)
   {
       lower_active_bound_of[i]=-1;
       upper_active_bound_of[i]=-1;
   }
   curL=0;curR=0;
   for(i=0;i<m;i++)
   {
       L=queries[i].l;
       R=queries[i].r;
       while(curR<=R)
       {
           Add(prefix_sum[curR],1);
           curR++;
       }
       while(curR > R+1)
       {
           Remove(prefix_sum[curR-1],1);
           curR--;
       }
       while(curL>L)
       {

           Add(prefix_sum[curL-1],0);
           curL--;
       }
       while(curL<L)
       {
           Remove(prefix_sum[curL],0);
           curL++;
       }
       ans[queries[i].id]=tree[1];
   }
   for(i=0;i<m;i++)
    pf("%d\n",ans[i]);
    return 0;
}
//10 1 10
//2 5 3 2 6 4 6 4 3 3
