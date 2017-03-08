#include <iostream>
using namespace std;

int VO(char c)
{
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}

bool match(string &A,string &B,int K)
{
    for(int i = 0; i < max(A.size(),B.size()); ++i)
    {
        if(A.size() <= i || B.size()<=i)return false;
        if(A[A.size()-1-i] != B[B.size()-1-i])
            return false;
        if(VO(A[A.size()-1-i]))K--;
        if(K==0)return true;
    }
    return false;
}

int type(string &A,string &B,string &C,string &D,int K)
{
    if(match(A,B,K) && match(A,C,K) && match(A,D,K))
        return 7;
    if(match(A,B,K) && match(C,D,K))
        return 1;//aabb
    if(match(A,C,K) && match(B,D,K))
        return 2;//abab
    if(match(A,D,K) && match(B,C,K))
        return 4;//abba
    return 0;
}

int main()
{
    int N, K;
    cin>>N>>K;
    int t = 7;
    for(int i = 0; i < N; ++i)
    {
        string A,B,C,D;
        cin>>A>>B>>C>>D;
        t &= type(A,B,C,D,K);
    }
    if(t==7)
        cout<<"aaaa"<<endl;
    else if(t==1)
        cout<<"aabb"<<endl;
    else if(t==2)
        cout<<"abab"<<endl;
    else if(t==4)
        cout<<"abba"<<endl;
    else 
        cout<<"NO"<<endl;

}