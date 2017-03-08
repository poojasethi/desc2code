#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
    char a[100],val;
    gets(a);
    cin>>val;
    cout<< count(a,a+strlen(a),val);
    return 0;
}
