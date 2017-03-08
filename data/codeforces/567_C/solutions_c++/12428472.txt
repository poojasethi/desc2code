#include <map>
#include <iostream>
using namespace std;
typedef long long int ll;

int main(){
	ll n, k;
	while(cin >> n >> k){
		ll gg = 0, elem;
		map <ll,ll> fir,sec;
		while(n--){
			cin >> elem;
			if(elem%k == 0){
				gg += fir[elem/k];
				fir[elem] += sec[elem/k];
			}
			sec[elem]++;
		}
		cout << gg << endl;
	}
}