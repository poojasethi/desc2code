#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,x,m,len=0,rep=0,arr[200005],last,temp;
    long long ans=1;
    scanf("%d",&n);
    for(int i=0;i<2*n;i++){
        scanf("%d",&arr[i]);
        if(i>=n && arr[i]==arr[i-n])
            rep++;
    }
    scanf("%d",&m);
    sort(arr,arr+2*n);
    for(int i=0;i<2*n;i++){
        if(arr[i]!=last)
            len=0;
        len++;
        temp=len;
        while(temp%2==0 && rep>0){
            temp/=2;
            rep--;
        }
        ans*=temp;
        ans%=m;
        last=arr[i];
    }
    printf("%I64d\n",ans);
    return 0;
}
