#include<iostream>
int reverse(int n){
    int rem=0;
    while(n>0){
    rem = (rem*10) + (n%10);
    n=n/10;
    }
    return rem;
}
int main(){
    int t,n;
    std::cin>>t;
    while(t--){
               std::cin>>n;
               n++;
               while(n!=reverse(n)){
                     n++;                                    
               }         
               std::cout<<n<<'\n';  
    }
    return 0;    
}
