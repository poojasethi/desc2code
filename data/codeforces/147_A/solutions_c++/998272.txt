#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string inp,rez;
int lst;

int main()
{
    getline(cin,inp);
    for(int i=0; i<inp.size();++i)
        if(isalpha(inp[i])) {
            if(lst) rez+=' ';
            rez+=inp[i],lst=0;
        }
        else if(' '==inp[i]) {
            lst=1;
        }else rez+=inp[i],lst=1;
    cout<<rez;
    return 0;
}
