#include <bits/stdc++.h>
using namespace std;

#define R(i,a,b) for(int i=a;i<b;i++)
#define RE(i,a,b) for(int i=a;i<=b;i++)
#define RR(i,a,b) for(int i=a;i>b;i--)
#define RRE(i,a,b) for(int i=a;i>=b;i--)
#define F(i,n) for(int i=0;i<n;i++)
#define FE(i,n) for(int i=0;i<=n;i++)
#define FR(i,n) for(int i=n;i>0;i--)
#define FRE(i,n) for(int i=n;i>=0;i--)
#define mp(a,b) make_pair(a,b)
#define pii pair <int, int>
#define pb push_back
#define ft first
#define sd second
#define LL long long
#define gc getchar_unlocked
#define pc putchar_unlocked

inline void get(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

inline void getll(LL &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

struct node
{
	LL left, right;

	node()
	{
		left = right = 0;
	}
};

struct node trie[800005]; 

void insert(LL a, LL k, LL root)
{
	if (k==0)
		return;

	if (k&a)
	{
		trie[root].right++;
		insert(a,k>>1,root*2+1);
	}
	else
	{
		trie[root].left++;
		insert(a,k>>1,root*2);
	}
}

LL query(LL q, LL k, LL root, LL lim)
{
	LL ans = 0;
	if (!k)
		return 0;

	if (k&lim)
	{
		if (k&q)
		{
			ans += trie[root].right;
			ans += query(q, k>>1, root*2, lim);
		}
		else
		{
			ans += trie[root].left;
			ans += query(q, k>>1, root*2+1, lim);
		}
	}
	else
	{
		if (k&q)
			ans += query(q, k>>1, root*2+1, lim);
		else
			ans += query(q, k>>1, root*2, lim);
	}
	return ans;
}

int main()
{
	LL T;
	getll(T);
	for (LL __rep = 1; __rep <=T; __rep++)
	{
		LL n,k;
		getll(n);
		getll(k);
		insert(0,1<<17,1); 	
		LL fxor = 0;
		LL ans = 0;
		F(i,n)
		{
			LL tmp;
			getll(tmp);
			fxor = fxor^tmp;

			ans += query(fxor,1<<17,1,k);

			insert(fxor,1<<17,1);
		}
		printf("%lld\n", ans);
		F(i,800001)
		{
			trie[i].right = trie[i].left = 0;
		}
	}
	return 0;
}