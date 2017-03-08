#include<iostream>
#include<cstring>
int max(int a,int b){
    return a>b?a:b;    
}
int main(){
    int n,i,ans;
    int l[100005];
    //std::string str;
    char str[6];
    std::cin>>n;
    memset(l,-1,sizeof(l));
    ans=0; 
    while(n--){  
               std::cin>>str;
               std::cin>>i;           
               if(strcmp(str,"found")==0) 
                   l[i]=ans;
               else if (l[i]>=0){
                    ans=max(ans,l[i]+i);
                    l[i]=-1;     
               }         
    }
    std::cout<<ans<<'\n';
    return 0;    
}
