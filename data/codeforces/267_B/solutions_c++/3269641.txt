#include<iostream>
using namespace std;
int a[7][7],ans[300],x[102],y[102],d[7];
int m;
void dfs(int x){
     for(int i=0;i<=6;++i){
        if(a[x][i]){a[x][i]--;a[i][x]--;dfs(i);}              
     }  
     ans[m--]=x;
}
int main(){
    int n,i,j,start,c=0;
    cin>>n;
    m=n+1; 
    for(i=1;i<=n;++i){
    cin>>x[i]>>y[i];
    a[x[i]][y[i]]++;a[y[i]][x[i]]++;
    d[x[i]]++;d[y[i]]++;              
    }
    start=x[1];
    for(i=0;i<=6;++i){
       if(d[i]&1){c++;start=i;}
    }
    if(c>2){
             cout<<"No solution\n";
             return 0;
    }
    dfs(start);
    if(m>0){
        cout<<"No solution\n";
        return 0;
    }
    for(i=1;i<=n;++i){
        for(j=1;j<=n;++j){
        if(ans[i]==x[j]&&ans[i+1]==y[j]){cout<<j<<" +\n";  x[j]=-1;y[j]=-1;break;}
        else if(ans[i]==y[j]&&ans[i+1]==x[j]){cout<<j<<" -\n"; x[j]=-1;y[j]=-1;break; }
      }
    }
    return 0;
}