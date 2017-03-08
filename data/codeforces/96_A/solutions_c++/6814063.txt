#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
    char s[101];
    gets(s);
    cout<<(strstr(s,"0000000") || strstr(s,"1111111") ? "YES":"NO");
}

