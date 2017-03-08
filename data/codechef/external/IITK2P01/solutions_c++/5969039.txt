#include<iostream>
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
	char ch[6]={-1};
	while(n>0){
		ch[i++]='0'+n%10;
		n=n/10;
	}
	while(i-->0){
		pc(ch[i]);
	}
	pc('\n');
}
int main(){
    
    int T,K;
    long long int N,r,count;
    
    //std::cin>>T;
    T = scan();
    
    while( T-- ){
           
           count = 0;
           //std::cin>>N>>K;  
           N = scan();
           K = scan();
           
           if( K == 1 )
               //std::cout<<N<<"\n";     
               print(N);
           
           else{
               while( N > 0 ){
                      
                      count += N%K;
                      N /= K;
               }
               //std::cout<<count<<"\n";
               print(count);
           }
    }
        
    return 0;
        
}
