#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T,N,K;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cin>>N;
        int *arr=(int *)malloc(N*sizeof(int));
        for(int j=0;j<N;j++)
            cin>>arr[j];
        cin>>K;
       int temp=arr[K-1];
        sort(arr,arr+N);
        for(int j=0;j<N;j++)
        {
            if(arr[j]==temp)
                cout<<j+1<<endl;
        }
    }
    return 0;
}
