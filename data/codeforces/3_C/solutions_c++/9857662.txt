#include <iostream>
using namespace std;
char a[5][5];
bool win(char c)
{
	int i;
	if (a[1][1]==c&&a[2][2]==c&&a[3][3]==c||a[1][3]==c&&a[2][2]==c&&a[3][1]==c) return true;
	for (i=1;i<=3;i++)
		if (a[i][1]==c&&a[i][2]==c&&a[i][3]==c||a[1][i]==c&&a[2][i]==c&&a[3][i]==c) return true;
	return false;
}
int main()
{
	int i,j,co=0,cx=0;
	for (i=1;i<=3;i++)
		for (j=1;j<=3;j++)
		{
			cin>>a[i][j];
			if (a[i][j]=='X') cx++; else if (a[i][j]=='0') co++;
		}
	if (co!=cx&&co!=cx-1||win('0')&&win('X')||win('0')&&co==cx-1||win('X')&&co==cx)
		cout<<"illegal";
	else if (win('X'))
		cout<<"the first player won";
	else if (win('0'))
		cout<<"the second player won";
	else if (cx+co==9)
		cout<<"draw";
	else if (cx==co)
		cout<<"first";
	else
		cout<<"second";
	return 0;
}
