#include <iostream>
#include <queue>
#include <stack>

using namespace std;

int main(){
int t;
cin>>t;
while(t--){
    long num,temp;
    int rem,div = 10;
    cin>>num;
    temp = num;
    stack<int> s;
    queue<int> q;
    bool isPalindrome = true;
    while(temp){
        rem = temp % div;
        temp = temp / div;
        q.push(rem);
        s.push(rem);
    }
    if(s.size() != q.size())
        break;
    else{
        while(!s.empty()){
             if(s.top() == q.front()){
                s.pop();
                q.pop();
             }
             else{
                isPalindrome = false;
                break;
             }
        }
        if(isPalindrome)
            cout<<"wins"<<endl;
        else
            cout<<"losses"<<endl;
    }
}
return 0;
}
