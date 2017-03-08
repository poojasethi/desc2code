
#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <locale>
#include <set>
#include <vector>

#define mod 1000000007
typedef long long int lld;

lld array[100005];

using namespace std;

lld get_power(lld a, lld b){

	if(b==0){
		return 1;
	}
	lld solution = 1;

	while(b>0){

		if(b%2==1){
			solution = (solution * a)%mod;
		}

		a = (a*a)%mod;
		b = b/2;
	}

	return solution;
}

int main(){

	lld test_cases, i, j, k;
	cin >> test_cases;

	while(test_cases){

		lld length;
		cin >> length;
		//now for each of the position it can be treated as i or j
		//that is giving us two options for each index
		//when the single element is left only way is there to permute and get the max element
		//in the indices
		lld solution = get_power(2, length-1);
		cout << solution << endl;
		test_cases--;
	}

	return 0;
}