#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int col,te,i,j,flag;
    char a[1000];
    while(1)
    {
        cin>>col;
        if(col == 0)
            break;
        cin>>a;
        int k =0;
        for(i=0;i<col;i++)
        {
            k = k+1;
            flag = 0;
            for(j = i;j<strlen(a);j+=col)
            {
                if(flag == 0)
                {
                    cout<<a[j];
                    flag = 1;
                }
                else
                {
                    cout<<a[j+col-k-i];
                    flag = 0;
                }
            }
        }
        cout<<"\n";
    }
    return 0;
}