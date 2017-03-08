#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstring>
#include <functional>
#include <iostream>
#include <unistd.h>
#include <utility>
#include <vector>
#include <map>
 
#define getw getchar_unlocked
#define iterate(n) for(i=0;i<n;i++)
#define d_iterate(p,q) for(int i=p;i<=q;i++)
#define r_iterate(n,z) for(int i=n-1;i>=n-z;i--) /* z number of elements to the left of n */
#define p(n) printf("%d\n",n);
#define get(n) n = scan2();
// #define sort(k,q) qsort(k,q,sizeof(*k),comp);
#define print_array(k,n) iterate(n){ p(k[i]);}
#define ps(s) printf("%s\n",s);
#define repeat(n) for (int i = (0); i < n; i++)
#define clear(v) memset((v), 0, sizeof (v))
#define ALL(x) (x).begin(), (x).end()
#define mp make_pair;
#define pb push_back;
// int comp(const void *e1,const void *e2){ return *((const lld *)e1) - *((const lld *)e2);}
 
typedef unsigned long long int lld;
typedef unsigned long int ld;
using namespace std;
 
inline lld scan2(){
	lld n=0,s=1;
	char p=getw();
	if(p=='-') s=-1;
	while((p<'0'||p>'9')&&p!=EOF&&p!='-') p=getw();
	if(p=='-') s=-1,p=getw();
	while(p>='0'&&p<='9') { n = (n<< 3) + (n<< 1) + (p - '0'); p=getw(); }
	return n*s;
}
 


// long long int modinv(long long int a, long long int m) {
//     return pow(a,m-2,m);
// } 

lld power(lld a,lld b,lld p){
	lld ans = 1;
	while(b){
		if(b&1)
			ans = (ans * a)%p;
		a = (a * a)%p;
		b >>= 1;
	}
	return ans;
}

lld solve(lld n, lld p){
	//all i need to find is n!%p 
	//Using wilson theorem , i.e (p-1)!%p = p-1 if p is prime

	lld i,j,k,ans,val ;

	if ( n>=p )  //easie piezy bcoz p already exist in the n! sequence , thus 0
		return 0;

	/*
		As we know 
			(p-1)!%p = p-1
		(p-1)! = (p-1)(p-2)(p-3).....(n+1)(n)! which is equal to p-1(as above stated)

		thus,
			(p-1)(p-2)(p-3)...n! = p-1;

		thus first find [(p-1)(p-2)(p-3)....(n+1)]%p and then inverse modulus to find the answer.
		"i still dont get this modular inverse.(fuck)"

	*/

	val = 1;	
	for( i=n+1;i<=p-1;i++){
		val = (val*i)%p;
	}

	/* val is (p-1)(p-2)...(n+1)
	
		now everything being done is for inverse modulus
	*/


	ans = power(val,p-2,p); // this works for modular inverese ( just a power function with  )

	ans = -1 * ans + p;
	ans  = ans%p;
	return ans;

}
 
int main(){
	lld i,z,n,j,k,t,h,ans = 0;
	lld a,b,c,d,p;

	// cout << power(2,10,10460);

	get(t);
	
	while(t--){
		get(n);
		get(p);
		printf("%lld\n",solve(n,p));
	}
 
	return 0;
}