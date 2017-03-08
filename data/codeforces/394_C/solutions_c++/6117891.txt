/****
	*@neko01
	*Title:C
	*/
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int a[1050][1050];
char s[5];
int main()
{
    int n,m;
    scanf("%d%d", &n, &m);
    int b = 0, c = 0, d = 0, e = 0;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            scanf("%s", s);
            if (s[0] == '0' && s[1] == '0') a[i][j] = 0, b++;
            if (s[0] == '0' && s[1] == '1') a[i][j] = 1, c++;
            if (s[0] == '1' && s[1] == '0') a[i][j] = 2, c++;
            if (s[0] == '1' && s[1] == '1') a[i][j] = 3, e++;
        }
    }
    int cc = c / 2;
    c -= cc;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (e)      { a[i][j]=3; e--; }
            else if (c) { a[i][j]=1; c--; }
            else if (cc && a[i-1][j] == 1) { a[i][j]=2; cc--; }
            else if (b) { a[i][j] = 0; b--; }
            else if (cc){ a[i][j] = 2; d--; }
            if (a[i][j] == 0)  printf("00 ");
            else if (a[i][j] == 1) printf("01 ");
            else if (a[i][j] == 2) printf("10 ");
            else printf("11 ");
        }
        printf("\n");
    }
    return 0;
}