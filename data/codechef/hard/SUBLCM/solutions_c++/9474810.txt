#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

#define getcx 			getchar//_unlocked
inline ll inp(){
	ll n=0;
	int ch=getcx();int sign=1;
	while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
	 
	while( ch >= '0' && ch <= '9' )
	n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
	n=n*sign;
	return n;
}

#define maxn 1000001
vi primes;
vi Factors[maxn];
void sieve(){
	bitset<maxn> b; b.set();
	for(int i=2; i<maxn; i++){
		if(!b[i])
			continue;
		primes.pb(i);
		for(ll j = i*1ll*i; j < maxn; j+=i)
			b[j] = false;
	}
}

void factorize(){
	Factors[1].pb(1); Factors[2].pb(2);
	for(int n=3; n<maxn; n++){
		bool isPrime = false; ll p=0;
		for(int i=0; i<primes.size();i++){
			p = primes[i];
			if(p*p > n){
				isPrime = true;
				break;
			}
			if(n % p == 0)
				break;
		}
		if(isPrime)
			Factors[n].pb(n);
		else{
			Factors[n] = Factors[n/p];
			if((n/p) % p != 0)
				Factors[n].pb(p);
		}
	}
}

int ar[100010];
int prev[maxn];
int dp[100010];

int Cal(int i){
	vi& v = Factors[ar[i]];
	int ans = 0;
	for(int j=0; j<v.size(); j++){
		ans = max(ans, prev[v[j]]);
		prev[v[j]] = i;
	}
	return ans;
}

int main(){
	sieve(); factorize();
	int t,n; t = inp();
	while(t--){
		n = inp();
		for(int i=1; i<=n; i++)
			ar[i] = inp();
		memset(prev, 0, 4*maxn);
		dp[0]=0; int ans = 0, idx;
		for(int i=1; i<=n; i++){
			idx = Cal(i);
			dp[i] = min(dp[i-1]+1, i-idx);
			ans = max(ans, dp[i]);
		}
		if(ans <= 1) ans = -1;
		printf("%d\n", ans);
	}
	return 0;
}