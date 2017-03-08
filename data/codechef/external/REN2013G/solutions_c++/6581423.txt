#include<bits/stdc++.h>
using namespace std;

#define pii pair<int,int>

int length[2222];
bool visited[2222];
int coord[2222][2];
int calc(int i,int b)
{
    return (coord[i][0]-coord[b][0])*(coord[i][0]-coord[b][0])+(coord[i][1]-coord[b][1])*(coord[i][1]-coord[b][1]);
}

priority_queue<pii> Q;
int main()
{
    int n,i,u,v;
    scanf("%d",&n);
    coord[0][0]=0;
    coord[0][1]=0;
    for(i=1;i<=n+1;i++)
    {
        scanf("%d%d",&coord[i][0],&coord[i][1]);
    }
    memset(length,1111111,sizeof(length));
    memset(visited,false,sizeof(visited));
    Q.push(pii(0,0));
    length[0]=0;
    while(!visited[n+1])
    {
         u=Q.top().second;
        int wt=-Q.top().first;
        Q.pop();
        if(length[u]<wt)
        continue;

        for(i=1;i<=n+1;i++)
        {
            if(!visited[i]&&wt+calc(i,u)<length[i])
            {
                length[i]=wt+calc(i,u);
                Q.push(pii(-length[i],i));
            }
        }
        visited[u]=true;
    }
    printf("%d\n",length[n+1]);
    return 0;
}
