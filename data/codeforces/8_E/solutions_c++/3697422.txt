#include<cstdio>
#include<cstring>
#include<iostream>
#define ll long long
#define N 55
bool v[N][2][2];
ll res,k,f[N][2][2];
char a[N]; int n;
ll cal(int l,int x,int y)
{
    ll &res=f[l][x][y]; if (v[l][x][y]) return res;
    v[l][x][y]=1,res=0; if (l+l>=n) return res=1;
    for (int i=0;i<2;i++) if (!a[l] || a[l]==i+48)
        for (int j=0;j<2;j++) if (!a[n-1-l] || a[n-1-l]==j+48)
            if ((l+l+1!=n || i==j) && (x||i<=j) && (y||i+j<2)) res+=cal(l+1,x||i<j,y||i+j<1);
    return res;
}
int main()
{
    std::cin>>n>>k,k++;
    if (cal(0,0,0)<k) return puts("-1"),0;
    for (int i=0;i<n;i++){
        a[i]='0'; memset(v,0,sizeof(v)); res=cal(0,0,0);
        if (res<k) k-=res,a[i]='1';
        }
    return puts(a),0;
}