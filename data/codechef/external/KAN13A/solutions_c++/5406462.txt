#include<bits/stdc++.h>
using namespace std;
int ar[105][205];
int dp[105][205];
int path[105][205];
string name[105];
int n,m;
int solve(int ind,int month) {
    //cout<<cost<<" "<<ind<<" "<<month<<endl;
    if(month==m) return 0;
    if(dp[ind][month]!=-1) return dp[ind][month];
    int ans=INT_MAX,index=-1;
    for(int i=0;i<n;i++) {
        int tc=0;
        if(i!=ind) tc=ar[i][month]-(ar[ind][month]-100);
        tc=tc+solve(i,month+1);
        if(tc<ans) {
            index=i;
            ans=tc;
        }
    }
    dp[ind][month]=ans;
    path[ind][month-1]=index;
    return ans;
}
vector<int> ans;
void build(int index,int mnt) {
    if(mnt==m) return;
    ans.push_back(index);
    build(path[index][mnt],mnt+1);
}
int main()
{
    string s,s1;
    cin>>s;
    while(s!="TheEnd") {
        cin>>n>>m;
        for(int i=0;i<n;i++) {
            cin>>s1;
            name[i]=s1;
            for(int j=0;j<m;j++) {
                cin>>ar[i][j];
                dp[i][j]=-1;
            }
        }
        int anss=INT_MAX,index=-1;
        for(int i=0;i<n;i++) {
            int z=ar[i][0]+solve(i,1);
            if(z<anss) {
                anss=z;
                index=i;
            }
        }
        cout<<s<<endl;
        cout<<"Tk "<<anss<<endl;
        ans.clear();
        //ans.push_back(index);
        build(index,0);
        //for(int i=0;i<m;i++) cout<<ans[i]<<" "; cout<<endl;
        for(int i=0;i<m;) {
            int j=i;
            int cnt=0;
            while(j<m && ans[j]==ans[i]) {
                j++;cnt++;
            }
            cout<<name[ans[i]]<<" for "<<cnt<<" month(s)\n";
            i=j;
        }
        cout<<endl;
        cin>>s;
    }
    cout<<"TheEnd\n";
    return 0;
}
