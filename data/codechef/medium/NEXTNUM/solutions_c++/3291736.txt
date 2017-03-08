/**
http://www.codechef.com/problems/NEXTNUM
*/

/**
INPUT:
2
276
762

OUTPUT:
2
6

*/

#include <cstdio>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <map>
#include <cstring>
using namespace  std;
#define N 6666
#define INF 1000000000
#define ull long long

//This is used t store the Factorial of Numbers upto 22.
ull fact[22];
//This is used to store the frequency of the Numbers that are present
//in the given Number.
int fq[11];

//string to store the number.
char s[22];

void factorial()
{
    int i,j;
    fact[0]=fact[1]=1;
    for(i=2;i<22;i++)
    {
        fact[i]=i*fact[i-1];
    }
}

//It returns the number of ways of permutations.
ull no_of_Permutation()
{
    int i,j,k;
    ull ans=0;
    for(i=0,j=0;i<11;i++)
    {
        j+=fq[i];
    }
    ans=fact[j];
    for(i=0;i<11;i++)
    {
        if(fq[i]>0)
        ans=ans/fact[fq[i]];
    }
    return ans;
}

//Function for calculating the string length..
int strlenn(char *s)
{
    int i=0;
    while(s[i++]);
    return i-1;
}

int main()
{
	//printf("\ndriver of NEXTNUM is running..\n");
	int i,j,k,t,l;
	ull ans;
	//Preprocess  all the factorials.
	factorial();
	scanf("%d",&t);
	while(t--)
	{
        scanf("%s",s);
        l=strlenn(s);

        //Reset the value of Frequency array.
        for(i=0;i<11;i++)
        fq[i]=0;

        for(i=0;i<l;i++)
        {
            fq[s[i]-'0']++;
        }

        ans=0;
        //now calculate the no of possible permutation at each index.
        for(i=0;i<l;i++)
        {
            k=s[i]-'0';
            for(j=0;j<k;j++)
            {
                if(fq[j]>0)
                {
                        //choose that number for that position , so that
                        //it would not be used by others.
                        fq[j]--;
                        ans+=no_of_Permutation();
                        //Again free that number
                        fq[j]++;
                }
            }
            //choose this number permanently for that position.
            fq[s[i]-'0']--;
        }
        printf("%lld\n",ans+1);
    }

    return 0;
}
