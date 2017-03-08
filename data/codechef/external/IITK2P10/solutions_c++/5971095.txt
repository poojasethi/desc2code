#include<iostream>
#include<cstdio>

#define gc getchar_unlocked
#define pc putchar_unlocked
#define ll long long
#define MOD 1000000007

/*ll scan(){
         
    ll n;
    
    char ch;
	ch = gc();
	while(ch<'0' || ch >'9')
		ch=gc();
	while(ch>='0' && ch<='9'){
		n=n*10+ch-'0';
		ch=gc();
	}
	
    return n;             
         
}

ll print( ll n ){
    
    ll i=0;
    
	char ch[20]={-1};
	
	while(n>0){
		ch[i++]='0'+n%10;
		n=n/10;
	}
	while(i-->0){
		pc(ch[i]);
	}
	pc('\n');      
        
}*/
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

ll pow(ll a, ll b , ll M){
     
    ll x=1,y=a;
    
    while(b > 0){
        
        if(b%2 == 1){
            x=(x*y);
            if(x>M) 
                      x%=M;
        }
        y = (y*y);
        
        if(y>M) 
                  y%=M;
        b /= 2;
    }
    return x;
    
}

int main(){
    
    ll T,N,K,res;
    
    T = scan();
    
    while( T-- ){
           
           K = scan();
           N = scan();
           
           
           if( N == 1 )
               std::cout<<"1\n";
           
           else if( N == 2 )
               print(K);     
           
           else{
                
                res =  pow( 2 , N-3 , MOD-1 ); 
               
                
                res = pow( K , res , MOD );
               
                print(res);
           }           
           
    }
        
    return 0;
        
}
