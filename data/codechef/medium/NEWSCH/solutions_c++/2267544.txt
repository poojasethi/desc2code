#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
#define MOD 1000000007
#define PR(x) cout << #x " = " << x << "\n";
inline int fast_int()
{
int n=0;
int ch=getchar();
while(ch<48)ch=getchar();
while(ch >47)
n=(n<<3)+(n<<1)+ch-'0',ch=getchar();
return n;
}
int64_t ipow(int n,int k){
	if (k==0)
	{
		return (int64_t)1;
	}

	if(k%2==0){
		int64_t temp = ipow(n,k/2);
		return (temp*temp)%MOD;
	}else{
		int64_t temp= ipow(n,k/2);
		return (temp*temp*n)%MOD;
	}
}
int main(){
	int64_t t;
	cin>>t;

	while(t--){
		int64_t n;
		cin>>n;

		cout<<ipow(3,n) + ((n%2==0)?3:(-3)) <<endl;
	}
}