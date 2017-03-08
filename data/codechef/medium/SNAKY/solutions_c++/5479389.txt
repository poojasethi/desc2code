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

int board[1005][1005];
char snake[1000005];

int main()
{
	int T;
	get(T);
	for (int __rep = 1; __rep <=T; __rep++)
	{
		memset(board, 0, sizeof(board));
		// memset(snake, '\0', sizeof(snake));
		int m, n, x, y, l, move = 0;
		bool flag = false;

		get(n);
		get(m);
		get(x);
		get(y);
		get(l);

		x--, y--;
		int ix = x, iy = y;
		board[x][y] = 1;

		scanf("%s",snake);

		F(i,l-1)
		{
			switch (snake[i])
			{
				case 'U' : y++; break;
				case 'D' : y--; break;
				case 'R' : x++; break;
				case 'L' : x--; break;
			}

			board[x][y] = 1;
		}

		int i=0;
		
		while(1)
		{
			board[ix][iy] = 0;
			
			if (i<l-1)
				switch (snake[i])
				{
					case 'U' : iy++; break;
					case 'D' : iy--; break;
					case 'R' : ix++; break;
					case 'L' : ix--; break;
				}

			switch (snake[l-2])
			{
				case 'U' : y++; break;
				case 'D' : y--; break;
				case 'R' : x++; break;
				case 'L' : x--; break;
			}

			if (x<0 || y<0 || x>=n || y>=m)
				break;

			if (board[x][y] == 1)
			{
				flag = true;
				break;
			}

			move++;
			board[x][y] = 1;
			i++;
		}

		if (flag)
			printf("BODY %d\n", move);
		else printf("WALL %d\n", move);
	}
	return 0;
}