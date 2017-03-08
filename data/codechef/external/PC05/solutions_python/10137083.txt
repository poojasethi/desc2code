#include <iostream>
#include <math.h>
using namespace std;
 
inline bool isPrime(int num){
    if(num == 1)
        return false;
    for(int i = 2; i <= sqrt(num); i++){
        if(num % i == 0)
            return false;
    }
    return true;
}
 
inline bool evaluate(int num){
    int sum_of_digits = 0;
    while(num >0){
        int digit = num % 10;
        sum_of_digits += digit;
        num /= 10;
    }
    
    if(isPrime(sum_of_digits)){
        return true;
    }
    else
        return false;
}
 
int main() {
	
	int T; //Number of test cases
	cin>>T;
	
	for(; T > 0; T--){
	 
	    int L, U, count = 0;
	    cin>>L>>U; //Lower bound and upper bound
	    
	    for(; L <= U; L++){
	        
	        if(evaluate(L))
	            count++;
	            
	    }
	    
	    cout<<count<<endl;
	 
	}
	return 0;
} 