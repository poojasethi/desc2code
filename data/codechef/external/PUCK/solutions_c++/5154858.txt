#include <bits/stdc++.h>
using namespace std;
#define PB push_back
int k;
struct node
{
    int odd_sum , even_sum,odd_count,even_count;
    vector<char> lazy ;
    void split(node &a , node &b)
    {
        for(int i=0;i<lazy.size();i++)
        {
            if(lazy[i] == 'E')
            {
                a.even_sum += a.odd_sum + a.odd_count;
                a.odd_sum = 0;
                a.even_count += a.odd_count;
                a.odd_count = 0;
                b.even_sum += b.odd_sum + b.odd_count;
                b.odd_sum = 0;
                b.even_count += b.odd_count;
                b.odd_count = 0;
                a.lazy.PB('E');
                b.lazy.PB('E');
            }
            else if(lazy[i] == 'O')
            {
                a.odd_sum += a.even_sum + a.even_count;
                a.even_sum = 0;
                a.odd_count += a.even_count;
                a.even_count = 0;
                b.odd_sum += b.even_sum + b.even_count;
                b.even_sum = 0;
                b.odd_count += b.even_count;
                b.even_count = 0;
                a.lazy.PB('O');
                b.lazy.PB('O');
            }
            else if(lazy[i] == 'I')
            {
                int temp;
                // left child
                temp = a.even_sum;
                a.even_sum = a.odd_sum + a.odd_count;
                a.odd_sum = temp  + a.even_count;
                temp = a.odd_count;
                a.odd_count = a.even_count;
                a.even_count = temp;

                // right child
                temp = b.even_sum;
                b.even_sum = b.odd_sum + b.odd_count;
                b.odd_sum = temp  + b.even_count;
                temp = b.odd_count;
                b.odd_count = b.even_count;
                b.even_count = temp;
                a.lazy.PB('I');
                b.lazy.PB('I');
            }
        }
        lazy.clear();
    }
    void point_update(char check)
    {
        if(check == 'E')
        {
            even_sum += odd_sum + odd_count;
            odd_sum = 0;
            even_count += odd_count;
            odd_count = 0;
            lazy.PB('E');
        }
        else if(check == 'O')
        {
            odd_sum += even_sum + even_count;
            even_sum = 0;
            odd_count += even_count;
            even_count = 0;
            lazy.PB('O');
        }
        else if(check == 'I')
        {
            int temp = even_sum;
            even_sum = odd_sum + odd_count;
            odd_sum = temp + even_count;
            temp = even_count;
            even_count = odd_count;
            odd_count = temp;
            lazy.PB('I');
        }
    }
    void merge(node a , node b)
    {
        even_sum = a.even_sum + b.even_sum;
        even_count = a.even_count + b.even_count;
        odd_sum = a.odd_sum + b.odd_sum;
        odd_count = a.odd_count + b.odd_count;
    }
    node()
    {
        odd_sum = 0;
        even_sum = 0;
        odd_count = 0;
        even_count = 0;
    }
}tree[2*(1<<20)];
void set_v(node &temp,int val)
{
    if(val&1)
    {
        temp.odd_sum += val;
        temp.odd_count +=1;
    }
    else
    {
        temp.even_sum += val;
        temp.even_count +=1;
    }
}
void create(int pos)
{
    pos>>=1;
    while(pos!=0)
    {
        tree[pos].merge(tree[pos*2],tree[pos*2 + 1]);
        pos>>=1;
    }
}
void range_update(int root,int left_most ,int right_most , int l,int r,char val)
{
    if(l <= left_most && r >= right_most){
        tree[root].point_update(val);
        return ;
    }
    int l_child = (root<<1) , r_child = l_child + 1 , mid = (left_most + right_most)>>1;
    tree[root].split(tree[l_child],tree[r_child]);
    if(l <= mid)
        range_update(l_child , left_most , mid , l , r , val);
    if(r > mid)
        range_update(r_child , mid+1 , right_most , l , r , val);
    tree[root].merge(tree[l_child] , tree[r_child]);
}
node range_query(int root , int left_most , int right_most , int l ,int r)
{
    if( l <= left_most && r >= right_most )
        return tree[root];
    int l_child = (root<<1) , r_child = l_child + 1 , mid = (left_most + right_most )>>1 ;

    tree[root].split(tree[l_child],tree[r_child]);

    node l_node = node() , r_node = node();

    if(l <= mid)
        l_node = range_query(l_child , left_most , mid , l , r);
    if(r > mid)
        r_node = range_query(r_child , mid + 1 , right_most, l , r);

    tree[root].merge(tree[l_child] , tree[r_child]);

    node temp = node();
    temp.merge(l_node,r_node);

    return temp;
}
int main()
{
    int n,temp,l,r;
    scanf("%d",&n);
    k = ceil(log(n)/log(2));
    int pos = (1<<k);
    for(int i=0;i<n;i++){
        scanf("%d",&temp);
        set_v(tree[pos+i],temp);
        create(pos+i);
    }
    int m;
    char c;
    scanf("%d",&m);
    while(m--)
    {
        scanf(" %c%d%d",&c,&l,&r);
        if(c=='M'){
            node hold;
            hold = range_query(1,1,pos,l,r);
            cout<<hold.even_sum + hold.odd_sum<<endl;
        }
        else{
            range_update(1,1,pos,l,r,c);
        }
    }
    return 0;
}