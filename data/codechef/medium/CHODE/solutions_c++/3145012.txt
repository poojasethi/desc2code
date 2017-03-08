//
//  CodeDecode1.cpp
//  
//
//  Created by Gaurav Gulzar on 30/12/13.
//
//

#include<iostream>
#include<cstring>
//#include<conio.h>
#include<climits>
#include<cstdio>
#include<fstream>
//#define cin fin
using namespace std;

int main()
{
    // ifstream fin;
    //fin.open("input.cpp");
    int test_case;
    cin>>test_case;
    while(test_case--)
    {
        char c[27],waste[50],str[150008];
        cin>>c;
        gets(waste);
        gets(str);
        
        //cout << waste << "\n\n";
        int a[26]={0};
        int w;
        int x=strlen(str);
        for(int j=0;j<x;j++)
        {
            if(!isalpha(str[j])) continue;
            w=(int)str[j]-97;
            if(w<0) w+=32;
            a[w]++;
        }
        char C[]="abcdefghijklmnopqrstuvwxyz";
        for(int i=0;i<26;i++)
            for(int j=i+1;j<26;j++)
                if(a[j]>=a[i])
                    swap(a[i],a[j]),swap(C[i],C[j]);
        int pos[26];
        for(int i=0;i<26;i++)
            pos[(int)C[i]-97]=i;
        for(int i=0;i<x;i++)
        {
            if(isalpha(str[i]))
            {
                if(isupper(str[i]))
                    str[i]=toupper(c[25-pos[(int)str[i]-65]]);
                else
                    str[i]=c[25-pos[(int)str[i]-97]];
            }
        }
        cout<<str<<"\n";
    }
    // getch();
    return 0;
}
