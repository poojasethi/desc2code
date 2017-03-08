#include <cstdio>
#include <cstring>

using namespace std;

const int MAX = (1 << 21);
const int OFFSET = (1 << 20);

struct RankSegTree
{
	int seg[2 * MAX];
	RankSegTree()
	{
		memset(seg, 0, sizeof(seg));
	}
	void insert(int v, int i)
	{
		for(i += MAX; i > 0; i /= 2) seg[i] += v;
	}
	int rank(int k)
	{
		int p;
		for(p = 1; p < MAX; )
		{
			//cout << 2*p << ' ' << seg[2*p] << endl;
			if(seg[2 * p] < k)
			{
				k -= seg[2 * p];
				p = 2 * p + 1;
			}
			else
			{
				p = 2 * p;
			}
		}
		return p - MAX;
	}
};


int N, M;
RankSegTree T;
int A[2 * MAX];
int assign[MAX];
bool used[MAX];
int nexti = 1;

int main()
{
	memset(used, 0, sizeof(used));
	memset(A, 0, sizeof(A));
	memset(assign, 0, sizeof(assign));

	scanf("%d %d", &N, &M);
	for(int i = 1; i <= N; i++)
	{
		A[OFFSET + i] = i;
		T.insert(1, OFFSET + i);
	}
	for(int m = 0; m < M; m++)
	{
		int x, y;
		scanf("%d %d", &x, &y);
		int i = T.rank(y);
		int v = A[i];
		if(assign[v] != x && (assign[v] != 0 || used[x]))
		{
			printf("-1");
			return 0;
		}
		assign[v] = x;
		used[x] = true;

		T.insert(-1, i);
		A[OFFSET - m] = v;
		T.insert(1, OFFSET - m);
	}

	for(int i = 1; i <= N; i++)
	{
		if(assign[i] != 0) printf("%d ", assign[i]);
		else
		{
			while(used[nexti]) nexti++;
			used[nexti] = true;
			printf("%d ", nexti);
		}
	}
}
