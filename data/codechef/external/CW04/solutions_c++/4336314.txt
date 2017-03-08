# include <stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>

using namespace std;

/* Function to swap values at two pointers */
void swap (char *x, char *y)
{
    char temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
  
/* Function to print permutations of string
   This function takes three parameters:
   1. String
   2. Starting index of the string
   3. Ending index of the string. */
void permute(char *a, int i, int n)
{
   int j;
   if (i == n)
     printf("%s\n", a);
   else
   {
        for (j = i; j <= n; j++)
       {
        //if((*(char *)(a+i) == *(char *)(a+j)) && (i != j)) continue;
          swap((a+i), (a+j));
          permute(a, i+1, n);
          swap((a+i), (a+j)); //backtrack
       }
   }
}
 
/* Driver program to test above functions */
int main()
{
   char a[100];
   cin>>a;
   int p=strlen(a);
   //sort(a,a+p);
   permute(a, 0, p-1);
   //getchar();
   return 0;
}