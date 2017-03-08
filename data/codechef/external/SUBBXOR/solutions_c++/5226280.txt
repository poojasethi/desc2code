// given an array and a number 'k', find the number of subsections whose XOR is less than k
// Using the idea in the prev prblm, this prblm is reduced to the following problem:
// Given an array find the number of pairs whose XOR is less than k
// How do we do that, we modify the query function a little.
// 

// given an array, find the subarray whose XOR is maximum
// F[L..R] = a[L]^a[L+1]^...^a[R]
// F[L..R] = F[1..L-1] ^ F[1..R]
// Hence if we have prefix xor's for all indices, we need to find those two indices whose xor is maximum

#include <bits/stdc++.h>
using namespace std;
#define g(n) scanf("%d",&n)
#define gl(n) scanf("%lld", &n)
#define f(i,n) for(int i=0; i<n; i++)
#define pb push_back
#define mp make_pair
#define fab(i,a,b) for(int i=a; i<=b; i++)
#define test(t) while(t--)
#define getcx getchar//_unlocked
typedef long long int lli;
struct node
{
	int nl, nr;
	node *left, *right;
}; 

// 0<=level<=31
void insert(node *v, int num, int level)
{
	// printf("At level %d for num = %d, made -> %d\n",level, num, v->num+1);
	if(level == -1)
	{
		return;
	}
	int k = num & (1<<level);
	if(k)
	{
		// printf("left\n");
		if(v->left == NULL)
		{
			node *temp = new node;
			temp->left = temp->right = NULL;
			temp->nl = temp->nr = 0;
			v->left = temp;
		}
		v->nl++;
		insert(v->left, num, level-1);
	}
	else
	{
		// printf("right\n");
		if(v->right == NULL)
		{
			node *temp = new node;
			temp->left = temp->right = NULL;
			temp->nl = temp->nr = 0;
			v->right = temp;
		}
		v->nr++;
		insert(v->right, num, level-1);
	}
}

// this function returns the number of numbers with whom xor with num is less than k
int query(node* v, int num, int level, int ans, int k)
{
	if(level==-1 || v==NULL)
		return ans;
	int p = num & (1<<level);
	p = (p>0)?1:0;
	int q = k & (1<<level);
	q = (q>0)?1:0;
	// if(level==2)
	// 	printf("%d, %d\n",p,q);
	if(level==0)
	{
		if(q==0)
			return ans;
		if(p==0)
		{
			int temp = v->nr;
			return ans + temp;
		}
		else
		{
			int temp = v->nl;
			return ans+temp;
		}
	}
	else if(p&q) //both are 1, p ^ 1 = 0, which will always be less than k. therefore trivial acceptance for left
	{
		int temp = v->nl;
		return query(v->right, num, level-1, ans+temp, k);
	}
	else if((!p) & q) // p=0, q=1, here p^0 =0, therefore, right is trivial accepting
	{
		int temp = v->nr;
		return query(v->left, num, level-1, ans+temp, k);
	}
	else if(p & (!q)) //p = 1, q=0. p^0=1, so right i trivial rejection
	{
		// int temp = (v->left==NULL) ? 0 : v->left->num;
		// printf("Yo %d, level = %d\n",temp,level);
		return query(v->left, num, level-1, ans, k);
	}
	else //p=0,q=0 p^1=1, so left is trivial rejection
	{
		return query(v->right, num, level-1, ans, k);
	}
}


void find_ans(int* ar, int len, int k)
{
	lli ans = 0;int p=0;
	node* root = new node;
	root->left = root->right = NULL;
	root->nl = root->nr =0;
	insert(root,0,31);
	f(i,len)
	{
		int q = p^ar[i];
		ans += (lli)query(root, q, 31, 0, k);
		insert(root, q, 31);
		p = q;
	}
	printf("%lld\n",ans);
}

int *ar;
int main()
{
	ar = new int[100005];
	int t,n,k;
	g(t);
	while(t--)
	{
		g(n),g(k);
		f(i,n) g(ar[i]);
		find_ans(ar,n,k);
	}
	return 0;
}