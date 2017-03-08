#include<iostream>
using namespace std;
int main()
{
    string s;
    char ch;
    cin>>s;
    int c=1,as,pc=0;
    ch=s[0];
    for(int i=1;i<s.size()+1;i++)
    {
        if(ch==s[i])
            c++;
        else
        {
            if(c==pc)
            {
                if(as>s[i-1]-'a')
                    as=s[i-1]-'a';
            }
            if(c>pc)
            {
                pc=c;
                as=s[i-1]-'a';
            }

            c=1;
            ch=s[i];
        }
    }
    cout<<char(97+as)<<endl<<pc<<endl;
    return 0;
}
