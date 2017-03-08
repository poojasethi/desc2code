#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int MAXBIT = 30;

struct Node
{
	Node* child[2];
	ll cnt;
	Node() { child[0] = child[1] = NULL; cnt = 0; }
};

Node* root;
int n, k, a[1000010], curXor;
ll res;

ll Count(Node* node, int bit)
{
	if (bit < 0)
		return 0;

	int bk = ((k >> bit) & 1), b = ((curXor >> bit) & 1);
	ll rr = 0;

	if (!bk && node->child[b^1] != NULL)
		rr = node->child[b^1]->cnt;

	if (node->child[b^bk] != NULL)
	{
		if (!bit)
			rr += node->child[b^bk]->cnt;
		else
			rr += Count(node->child[b^bk], bit-1);
	}
	return rr;
}

void Update(Node* node, int bit)
{
	if (bit < 0)
		return;

	int b = ((curXor >> bit) & 1);

	if (node->child[b] == NULL)
		node->child[b] = new Node();
	++(node->child[b]->cnt);
	Update(node->child[b], bit-1);
}

int main()
{
	root = new Node();

	scanf("%d %d", &n, &k);
	Update(root, MAXBIT);

	for (int i = 1; i <= n; ++i)
	{
		scanf("%d", a+i);
		curXor ^= a[i];
		res += Count(root, MAXBIT);
		Update(root, MAXBIT);
		// printf("%d %lld\n", i, res);
	}

	printf("%lld", res);
	return 0;
}