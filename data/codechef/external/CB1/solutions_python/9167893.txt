#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long int
using namespace std;

ll MAX = 1000001;
ll MOD = 1000000007;

bool primes[1000001];
int county[1000001];

void gen_primes()
{
		int i,j;
		for(i=2;i<=MAX;i++)primes[i] = 1;
		for(i=2;i<=(int)sqrt(MAX);i++)
			if(primes[i])
				for(j=i;j*i<=MAX;j++) primes[i*j] = 0;

        for(i=2;i<=MAX;i++)
            {
            if(primes[i])
            county[i]=county[i-1]+1;
            else
            county[i]=county[i-1];
        }
}
int main()
{
    ios_base::sync_with_stdio(0);
    int t,l,r,k;
    gen_primes();
    cin>>t;
    while(t--)
    {
        cin>>l>>r;
        cout<<county[r]-county[l-1]<<endl;
    }
    return 0;
}
