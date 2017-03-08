#include <iostream>
using namespace std;

int board[9][9];
int bBoard[9][9];
int best, N, M;

void saveBoard()
{
	for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
			bBoard[i][j] = board[j][i];
}

void printBoard()
{
	for(int i=0;i<N;i++, cout << endl)
		for(int j=0;j<M;j++)
			cout << (char)(bBoard[i][j]+'A'=='A'?'.':bBoard[i][j]+'A'-1);
}

int dx[][5] =
{
	{0, -1, -2, -1, -1},
	{-2, 0, -1, -2, -2},
	{-1, -1, 0, -1, -2},
	{0, 0, -1, -2, 0},
};

int dy[][5] =
{
	{0, 0, 0, -1, -2},
	{0, -1, -1, -1, -2},
	{0, -1, -2, -2, -2},
	{0, -1, -1, -1, -2},
};

bool place(int x, int y, int cur, int t)
{
	for(int i=0;i<5;i++)
	{
		int nx=x+dx[t][i], ny=y+dy[t][i];
		if(nx<0 || ny<0 || board[nx][ny])
			return false;
	}
	
	for(int i=0;i<5;i++)
	{
		int nx=x+dx[t][i], ny=y+dy[t][i];
		board[nx][ny] = cur;
	}
	return true;
}

void unplace(int x, int y, int cur, int t)
{
	for(int i=0;i<5;i++)
	{
		int nx=x+dx[t][i], ny=y+dy[t][i];
		board[nx][ny] = 0;
	}
}

void search(int x, int y, int cur)
{
	if(M*(N-y)+M-x<=5*(best-cur))
		return;
	
	if(x==M)
	{
		y++;
		x=0;
	}
	if(y==N)
	{
		if(cur>best)
		{
			best=cur;
			saveBoard();
		}
		return;
	}
	
	for(int i=0;i<4;i++)
	{
		if(place(x, y, cur, i))
		{
			search(x+1,y,cur+1);
			unplace(x, y, cur, i);
		}
	}
	search(x+1, y, cur);
}

int main()
{
	cin >> N >> M;
	search(0, 0, 1);
	cout << (best-1) << endl;
	printBoard();
	
	return 0;
}

