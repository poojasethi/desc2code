#include<iostream>
#include<algorithm>
int main(){
    int t,n,d;
    int points[52];
    std::cin>>t;
    while(t--){
               std::cin>>n;           
               for(int i=0;i<n;i++){
                   std::cin>>points[i];
                   points[i]*=3;        
               }
               for(int i=0;i<n;i++){
                   std::cin>>d;
                   points[i]+=d;        
               }
               std::sort( points, points + n );
               std::cout<<points[n-1]<<'\n';
    }
    return 0;    
}
