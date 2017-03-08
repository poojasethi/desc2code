#include <algorithm>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

#define sd(x) scanf("%d",&x)

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define PI pair< int , int >
#define INF 1000000000

#define MAXN 100010
#define MAXQ 100010

bool ans_this[MAXQ] = {0};
int no_chefs,no_queries;
int lefT,righT,mid,ret;
int BIT_deaths[MAXQ] = {0},ans[MAXQ] = {0},health[MAXN],BIT_poisons[MAXQ] = {0},my_stack[MAXN],pos[MAXN],no_inferiors[MAXN],temp[MAXN];
vector<int> inferior[MAXN];
vector<PI> vector_poisons[MAXN],vector_queries[MAXN];

inline void UpdateDeaths(int i){
    if (i == 0){
        return ; // just prev ention of crashing in case passing i = 0;
    }
    while (i <= no_queries){
        BIT_deaths[i] ++;
        i += (i&(-i));
    }
}

inline int QueryDeaths(int i){
    ret = 0;
    while (i > 0){
        ret += BIT_deaths[i];
        i -= (i&(-i));
    }
    return (int)ret;
}

inline void UpdatePoisons(int i,int val){
    if (i == 0)
    {
        return ; // just prevention of crashing in case passing i = 0;
    }
    while (i <= no_queries){
        BIT_poisons[i] += val;
        i += (i&(-i));
    }
}

inline int QueryPoisons(int i){
    ret=0;

    while (i > 0){
        ret += BIT_poisons[i];
        i -= (i&(-i));
    }

    return ret;
}

inline int Searchdeath(int health){

    if (QueryPoisons(no_queries) < health){
        return INF;
    }

    lefT = 1;
    righT = no_queries;

    while (lefT < righT){

        mid = (lefT + righT) / 2;

        if (QueryPoisons(mid) >= health){
            righT = mid;
        }
        else {
            lefT = mid+1;
        }
    }

    return righT;
}

inline void ProcessData(){
    int cur_pos,i,j,node,top;
    // DFS START
    top = 0;
    my_stack[top] = 0;
    cur_pos = 0;

    while(top >= 0){
        node = my_stack[top];
        top--;
        pos[node] = cur_pos;
        cur_pos++;

        for (i = inferior[node].size() - 1;i >= 0;i--){
            my_stack[++top] = inferior[node][i];
        }
    }
    // DFS END
    for (i = no_chefs;i >= 0;i--){
        no_inferiors[i] = 0;
        for (j = inferior[i].size() - 1;j >= 0;j--){
            no_inferiors[i] += no_inferiors[inferior[i][j]] + 1;
        }
    }

    for(i = 1;i <= no_chefs;i++){
        temp[i] = health[i];
    }
    for(i = 1;i <= no_chefs;i++){
        health[pos[i]] = temp[i];
    }

    return;
}

int main(){

    int i,s,j,a,x,typ,superior;

    sd(no_chefs);

    for (i = 1;i <= no_chefs;i++){
        sd(health[i]); sd(superior);
        inferior[superior].PB(i);
    }

    ProcessData();

    sd(no_queries);

    for (i = 1;i <= no_queries;i++){
        sd(typ);
        if (typ == 1){
            sd(a);
            sd(x);
            vector_poisons[pos[a]+1].PB(MP(i,x));              // storing the difference of poison sickness in vector
            vector_poisons[pos[a]+no_inferiors[a] + 1].PB(MP(i,-x));      // storing the difference of poison sickness in vector
        }
        else {
            sd(a);
            vector_queries[pos[a]].PB(MP(i,1));                // storing the query numbers in vector, if  number stored with it is 1 it is starting index
            vector_queries[pos[a]+no_inferiors[a]].PB(MP(i,2));         // storing the query numbers in vector, if  number stored with it is 2 it is ending index
            ans_this[i] = true;                                 // bool value for giving output or not
            ans[i] = no_inferiors[a];
        }
    }

    for (i = 1;i <= no_chefs;i++){

        for (j = vector_poisons[i].size() - 1;j >= 0;j--){
            UpdatePoisons(vector_poisons[i][j].F,vector_poisons[i][j].S); // Updating poison sickness from starting index of the person one by one
        }

        UpdateDeaths(Searchdeath(health[i]));  // SearchDeath(health[i]) finds the day on which a person of health health[i] Dies, and the death day is updated

        s = vector_queries[i].size();

        for (j = 0;j < s;j++){
            if (vector_queries[i][j].S == 1){ // QueryDeaths returns how many
                ans[vector_queries[i][j].F] += QueryDeaths(vector_queries[i][j].F); // if it is starting index of query then it is added to answer
            }
            else {
                ans[vector_queries[i][j].F] -= QueryDeaths(vector_queries[i][j].F); // if it is ending index of query then it is subracted to answer
            }
        }
    }

    for (i = 1;i <= no_queries;i++){
        if (ans_this[i] == true){
            printf("%d\n",ans[i]);
        }
    }
    return 0;
}
