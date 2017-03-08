#include<iostream>
#include<math.h>
using namespace std;

void checkprime( int i)
{
     if(i == 2)
    {
        cout<<i<<"\n";
        return;
    }
    if(i%2 == 0)
        return;
    else{
            if(i%2!=0 && i!=1)
            {
                      int f = sqrt(i);
                    for( int j=3;j<=f;j+=2)
                    {

                        if( i%j == 0)
                        {
                            return;
                        }
                    }
               cout<<i<<"\n";
            }
    }

}

void prime(  int m,   int n)
{
        for( int i=m;i<=n;i++)
        {
                checkprime(i);
        }
}

int main() {

    int t;
    cin>>t;
    while(t--)
    {
          int n,m;
        cin>>m>>n;
        prime(m,n);
        cout<<"\n";

    }
}
