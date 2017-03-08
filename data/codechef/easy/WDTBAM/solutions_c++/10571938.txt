#include<bits/stdc++.h>
using namespace std;

int main(){
    int T;
    cin>>T;
    while(T--){
            int i,N,count=0;
            long win=-1;
            cin>>N;
            string str,str1;
            cin>>str>>str1;
            long W[N+1];
            for(i=0;i<N+1;i++){
                  cin>>W[i];
                  }
            i=0;
            while(str[i]!='\0'){
                    if(str[i]==str1[i]){
                                       count++;
                                       }
                    i++;
                    }
            if(count!=N){
                        int max=W[0];
                        for(int i=0;i<=count;i++){
                            if(max<W[i]){
                                max=W[i];
                            }
                        }
                        cout<<max;
                        }
            else{
                 cout<<W[N];
                 }
            cout<<endl;
            }
    return 0;
    }
