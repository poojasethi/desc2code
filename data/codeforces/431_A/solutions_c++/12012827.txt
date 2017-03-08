#include<iostream>

using namespace std;

int main(){
    int four[4],sum=0;
    for(int i = 0;i<4;i++) cin>>four[i];
    char x;
    while(cin >> x){
        sum += four[x-'0'-1];
    }
    cout << sum;
}