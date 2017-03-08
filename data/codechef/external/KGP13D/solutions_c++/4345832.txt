#include <iostream>
#include <vector>
#include <queue>
#include <fstream>

using namespace std;

#define MAXN 200
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define INF 1000000007

int rev[MAXN + 2], cost[MAXN + 2], ti[MAXN + 2], nei[MAXN + 2], group_count, dp[MAXN + 2][MAXN + 2], ele[MAXN + 2][MAXN + 2], total_time[MAXN + 2][MAXN + 2];
bool vis[MAXN + 2];
pair<int, int> back_track[MAXN + 2][MAXN + 2];

vector<int> groups[MAXN + 2];

inline void BFS(int x){
    queue<int> Q;
    Q.push(x);
    vis[x] = true;
    groups[group_count].PB(x);
    int top;
    while(!Q.empty()){
        x = Q.front();
        if(vis[nei[x]] == false and nei[x] != -1){
            Q.push(nei[x]);
            vis[nei[x]] = true;
            groups[group_count].PB(nei[x]);
        }
        Q.pop();
    }
    group_count++;
    return;
}

inline void Solve(){
    group_count = 0;
    int n, i, j, k, x, y, d;
    for(i = 0; i <= MAXN; i++){
        vis[i] = false;
        groups[i].clear();
        nei[i] = rev[i] = -1;
    }
    cin>>n;
    for(i = 1; i <= n; i++){
        cin>>ti[i];
    }

    for(i = 1; i <= n; i++){
        cin>>cost[i];
    }

    cin>>k;
    for(i = 1; i <= k; i++){
        cin>>x>>y;
        nei[x] = y;
        rev[y] = x;
    }

    for(i = 1; i <= n; i++){
        if(vis[i] == false and rev[i] == -1){
            BFS(i);
        }
    }

    for(i = 0; i < group_count; i++){
        for(j = 0; j < groups[i].size(); j++){
            //cout<<groups[i][j]<<" ";
        }
        //cout<<endl;
    }

    int count = 1;
    vector<int> main_group;
    for(i = 0; i < groups[0].size(); i++){
        main_group.PB(groups[0][i]);
    }

    for(i = 0; i <= MAXN; i++){
        for(j = 0; j <= MAXN; j++){
            dp[i][j] = total_time[i][j] = 0;
        }
    }

    int val1, val2, i1, j1;
    vector<int> temp_group;
    while(count < group_count){
        temp_group.clear();
        for(j = 0; j <= main_group.size(); j++){
            for(i = 0; i <= groups[count].size(); i++){
                i1 = i - 1;
                j1 = j - 1;
                if(i == 0 and j == 0){
                    continue;
                }

                if(j == 0){
                    dp[i][j] = dp[i - 1][j]  + cost[groups[count][i1]] * (total_time[i - 1][j] + ti[groups[count][i1]]);
                    total_time[i][j] = total_time[i - 1][j] + ti[groups[count][i1]];
                    back_track[i][j] = MP(i - 1, j);
                    ele[i][j] = groups[count][i1];
                    continue;
                }
                if(i == 0){
                    dp[i][j] = dp[i][j - 1]  + cost[main_group[j1]] * (total_time[i][j - 1] + ti[main_group[j1]]);
                    total_time[i][j] = total_time[i][j - 1] + ti[main_group[j1]];
                    back_track[i][j] = MP(i, j - 1);
                    ele[i][j] = main_group[j1];
                    continue;
                }
                val1 = dp[i][j - 1]  + cost[main_group[j1]] * (total_time[i][j - 1] + ti[main_group[j1]]);
                val2 = dp[i - 1][j]  + cost[groups[count][i1]] * (total_time[i - 1][j] + ti[groups[count][i1]]);
                if(val1 < val2){
                    dp[i][j] = val1;
                    total_time[i][j] = total_time[i][j - 1] + ti[main_group[j1]];
                    back_track[i][j] = MP(i, j - 1);
                    ele[i][j] = main_group[j1];
                }
                else{
                    dp[i][j] = val2;
                    total_time[i][j] = total_time[i - 1][j] + ti[groups[count][i1]];
                    back_track[i][j] = MP(i - 1, j);
                    ele[i][j] = groups[count][i1];
                }
            }
        }
        i = groups[count].size();
        j = main_group.size();
        int temp_count = i + j;
        //cout<<"---------"<<count<<"---------"<<endl;
        while(!(i == 0 and j == 0)){
            temp_group.PB(ele[i][j]);
            i1 = back_track[i][j].F;
            j1 = back_track[i][j].S;
            //cout<<i<<" "<<j<<endl;
            i = i1;
            j = j1;
        }
        main_group.clear();
        for(i = temp_group.size() - 1; i >= 0; i--){
            main_group.PB(temp_group[i]);
        }
        count++;
        for(i = 0; i < main_group.size(); i++){
            //cout<<main_group[i]<<" ";
        }
        //cout<<endl;

    }
    int ans = 0, add_time = 0;
    for(i = 0; i < main_group.size(); i++){
        add_time += ti[main_group[i]];
        ans += add_time * cost[main_group[i]];
    }
    cout<<ans<<endl;
    return;
}

int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
    #endif
    int t, tt = 0;
    cin>>t;
    while(t--){
        tt++;
        cout<<"Case "<<tt<<": ";
        Solve();
    }
    return 0;
}
