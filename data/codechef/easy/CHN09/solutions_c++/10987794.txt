#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    { char s[100];
       int i,count1=0,count2=0;
       scanf("%s",s);
       for(i=0;s[i]!='\0';i++)
       {if(s[i]=='a')
        count1++;
        else 
        count2++;
        }
        if(count1>count2)
        cout<<count2<<'\n';
        else
        cout<<count1<<'\n';
        }
}           
         
