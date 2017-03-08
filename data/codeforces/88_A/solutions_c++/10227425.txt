#include<iostream>
#include<string>
using namespace std;
int main(){
    string s[12]={"C","C#","D","D#","E","F","F#","G","G#","A","B","H"},a,b,c;
    int i,x[12]={0};
    bool check=false;
    cin>>a>>b>>c;
    for(i=0;i<12;i++)
    {
    if ( a==s[i] || b==s[i] || c==s[i] )
    {
            x[i]=1;
    }
    }
    for(i=0;i<12;i++)
    {
        if (x[i])
        {

    if( x[(i+4)%12] && x[(i+7)%12] )
    {
        cout<<"major";
        check=true;
        break;
    }
    if( x[(i+3)%12] && x[(i+7)%12] )
        {
        cout<<"minor";
        check=true;
        break;
        }
    }
    }
    if (check==false)
    {
    cout<<"strange";
    }
    return 0;
}
