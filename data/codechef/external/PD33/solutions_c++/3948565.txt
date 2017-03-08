#include<iostream>
#include<deque>
#include<string>
using namespace std;
int printSolution(int,string);
int main()
{
    int n,k=0,i;
    deque<int> colDeque;
    deque<string> strDeque;
    while(1)
    {
        cin>>n;
        if(n==0)
            break;
        else
        {
            colDeque.push_back(n);
            string str;
            cin>>str;
            strDeque.push_back(str);
            k++;
        }
    }
    for(i=0;i<k;i++)
        if(i==0)
            printSolution(colDeque[i],strDeque[i]);
        else
        {
            cout<<endl;
            printSolution(colDeque[i],strDeque[i]);
        }

}
int printSolution(int n, string s)
{
    int noofrows,k=0,i,j;
    noofrows = s.size()/n;
    char a[noofrows][n];
    for(i=0;i<noofrows;++i)
    {
        for(j=0;j<n;++j)
        {
            if(i%2==0)
                a[i][j] = s[k];

            else if(i%2!=0)
                a[i][n-1-j] = s[k];
            k++;
        }
    }
    for(i=0;i<n;++i)
    {
        for(j=0;j<noofrows;++j)
            cout<<a[j][i];
    }
}
