#include <iostream>
using namespace std;

char board[101][101];
int piles[101];

int main()
{
	int n,m,k;
	cin >> n >> m >> k;
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			cin >> board[i][j];
	
	int c;
	bool flag,sr,sg,R=false,G=false;
	for(int i=0;i<n;i++)
	{
		flag=sr=sg=false;
		for(int j=0;j<m;j++)
		{
			if(flag)
				piles[i]++;
			sr|=board[i][j]=='R';
			sg|=board[i][j]=='G';
			if(board[i][j]=='R' || board[i][j]=='G')
				flag=!flag;
		}
		if(flag && m>1)
			R|=sr, G|=sg, piles[i]=0;
		if(!flag && m>2 && (sr ^ sg))
			R|=sr, G|=sg, piles[i]=0;
		if(piles[i]!=0)
			piles[i]--;
	}
	if(R&&G)
		cout << "Draw" << endl;
	else if(R)
		cout << "Second" << endl;
	else if(G)
		cout << "First" << endl;
	else
	{
		flag=true;
		for(int mask=1;mask<=m;mask<<=1)
		{
			c=0;
			for(int i=0;i<n;i++)
				c+=(piles[i]&mask)>0;
			if(c%(k+1))
			{
				flag=false;
				break;
			}
		}
		if(flag)
			cout << "Second" << endl;
		else
			cout << "First" << endl;
	}
	return 0;
}

