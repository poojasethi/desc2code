#include<iostream>

#define MOD 1000000007
#define ll long long
#define gc getchar_unlocked
#define pc putchar_unlocked
 
long long int scan(){
	long long int n=0;
	char ch;
	ch=gc();
	while(ch<'0' || ch >'9')
		ch=gc();
	while(ch>='0' && ch<='9'){
		n=n*10+ch-'0';
		ch=gc();
	}
		return n;
}

long long int print(long long int n){
	long long int i=0;
	char ch[150]={-1};
	while(n>0){
		ch[i++]='0'+n%10;
		n=n/10;
	}
	while(i-->0){
		pc(ch[i]);
	}
	pc('\n');
}

ll pow(ll a, ll b){
     
    ll x=1,y=a;
    
    while(b > 0){
        
        if(b%2 == 1){
            x=(x*y);
            if(x>MOD) 
                      x%=MOD;
        }
        y = (y*y);
        
        if(y>MOD) 
                  y%=MOD;
        b /= 2;
    }
    return x;
    
}

int main(){
    
    ll T,N,M,res;
    
    T = scan();
    
    while( T-- ){
           
           N = scan();
           M = scan();
           
           if( N == 1 ){
               res = M%MOD;
           }
               
           else if( N == 2 ){
               res = (M*(M-1))%MOD;
           }
           
           else{
                res = ((M*(M-1)) % MOD * pow(M-2,N-2) ) % MOD;     
           }               
          std::cout<<res<<"\n"; 
    }
    
    return 0;
        
}
