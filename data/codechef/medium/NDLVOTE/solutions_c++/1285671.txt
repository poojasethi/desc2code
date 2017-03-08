#include <iostream>
#include<cstdlib>
using namespace std;

int main()
{
    int n;
    long long int p,x;
    char c;
    while(1)
    {
        cin>>n;
        if(n==0)
        return 0;
        p=0;
        while(n--)
        {
        cin>>c>>x;
        if(c=='P')
        x--;
        else if(c=='M')
        x++;
       if(p%2==0)
        {
           if(x%2!=0&&x<p&&x>-p)
            p++;
             else
            {
                if(x>p)
                p=p+(x-p);
                else if(x<-p)
                p=p+abs(x+p);
            }
        }
        else if(p%2!=0)
        {
            if(x%2==0&&x<p&&x>-p)
            p++;
            else
            {
                if(x>p)
                p=p+(x-p);
                else if(x<-p)
                p=p+abs(x+p);
            }
        }
        }
        cout<<p<<endl;
    }
    return 0;
}

