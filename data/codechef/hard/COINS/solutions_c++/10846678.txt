#include<iostream>
using namespace std;

long long int mem[10000001] = {0};
long long int k;

long long int func(long long int n) {

    if(n<12) {
        return n;
    }
    else if(n == 12) {
        return 13;
    }
    else if(n<1000000) {

        if(mem[n]!=0){
            return mem[n];
        }

    }
    k = func((long long)n/2)+func((long long)n/3)+func((long long)n/4);
    if(n<1000000) {
        mem[n]=k;
    }
    return k;

}

int main() {

    long long int n1;

    while(cin>>n1){
       cout<<func(n1)<<"\n";

    }


}
