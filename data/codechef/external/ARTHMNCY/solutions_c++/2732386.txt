#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>

#define MAX 10000020
#define MOD 10007
#define INT_ITER vector<int>::iterator 

typedef long long ll;

using namespace std;

class Primes{
	vector<int> primes;

	public:

	Primes(int max){
		primes.clear();
		generatePrimes(max); 
	}

	void seive_mark(int prime, int start, int end, vector<bool>& range){
		int i = prime*prime;
		if (i < start){
			i = start;
			int extra = (start%prime); 
			if (extra){
				if ((start/prime) & 1)
					i += 2*prime - extra;
				else
					i += prime - extra;
			}
		}

		i = (i - start)/2;
		end = (end - start)/2;
		for (;i <= end; i+=prime) range[i] = false;
	}

	void generatePrimes(int end){
		if (!(end & 1)) end -= 1;
		int maxSeiveIndex = ((int)sqrt(end) - 3)/2 + 1;
		int maxPrimeIndex = (end-3)/2 + 1;

		vector<bool> range(maxPrimeIndex, true);
		primes.push_back(2);
		primes.push_back(3);
		for (unsigned j = 1; j < primes.size(); j++){
			seive_mark(primes[j], 3, end, range);
			int i;
			for (i = (primes[j] - 3)/2 + 1; i < maxSeiveIndex && !range[i]; i++);
			if (i < maxSeiveIndex){
				int next_prime = 3 + 2*i;
				primes.push_back(next_prime);
			}
			else
				break;
		}
		for(int i = maxSeiveIndex; i < maxPrimeIndex; i++)
			if (range[i]) primes.push_back(3+ 2*i);	
	}

	void print(){
		for(INT_ITER it = primes.begin(); it != primes.end(); it++) cout << *it << " ";
		cout << endl;
	}

	int findNumberOfPrimesLessThanEqualTo(int n){
		INT_ITER it = upper_bound(primes.begin(), primes.end(), n);
		return it-primes.begin();
	}
};


ll modExp(ll base, int exp){
	ll result = 1;
	while(exp){
		if (exp & 1) result = (result*base)%MOD;
		exp >>= 1;
		base = (base*base)%MOD;
	}
	return result;
}

int main(){
	Primes primes(MAX);
	int N;
	while(scanf("%d", &N) != EOF){
		if (N == 1)
			printf("%d\n", 0);
		else{
			int k = primes.findNumberOfPrimesLessThanEqualTo(N);
			printf("%lld\n", modExp(2,k-1));
		}
	}
	return 0;
}
