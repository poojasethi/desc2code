#include<bits/stdc++.h>
using namespace std;
char str[200000],*p;
int main()
{
    cin>>str;
    if((p=strstr(str,"AB")) && (strstr(p+2,"BA")))puts("YES");
    else if((p=strstr(str,"BA")) && strstr(p+2,"AB"))puts("YES");
    else puts("NO");
    return 0;
}
