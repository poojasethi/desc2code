#include <iostream>
#include <string>
using namespace std;
int main()
{
    while(1)
    {
    int col;
    cin >> col;
    if (col==0)
        break;
    else
    {
        string a;

        cin>>a;

        int n = a.size();
        int row = n/col;
        char arr[row][col];

        int i=0, j=0, m=0;
        for (i;i<row;i++)
        {   j=0;
            while (j<=col-1)
            {
                arr[i][j] = a[m];
                j++; m++;
            }
            i++;
            j--;
            while(j!=-1)
            {
                arr[i][j] = a[m];
                j--; m++; //if (j==-1) break;
            }

        }

        for (int x=0; x<col; x++)
        {
            for (int y=0; y<row; y++)
            {
                cout << arr[y][x];
            }
        }
        cout << endl;


    }
    }
}
