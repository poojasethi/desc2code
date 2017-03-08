# include <stdio.h>
#include<iostream>
#include<vector>
 #include<string.h>
 #include<algorithm>
 
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

int counter = 0;
void permute2(char *a, int length)
 {
    if(length == 0) 
	{
        printf("%s\n",a);
        ++counter;
        return;
    }
	else
	{
        // Find the smallest char in the string set it to be the first character. Solve the subproblem for the smaller string.
        char *smallest = min_element(a, a + length);
        swap(a, smallest);
        permute2(a+1, length-1);
        
        // Look for the smallest element strictly greater than the first element of the current string
        char *smallest_greater = a + length;
        for(char *i = a+1; i != a+length; ++i)
            if(*i > *a && (smallest_greater == a+ length || *i < *smallest_greater))
                smallest_greater = i;
        while(smallest_greater != a+length) {
            // If such an element is found, swap it into the first slot and recurse
            swap(a, smallest_greater);
            permute2(a+1, length-1);

            // Repeat the loop if possible for the next greater character
            smallest_greater = a+ length;
            for(char *i = a+1; i != a+length; ++i)
                if(*i > *a && (smallest_greater == a + length || *i < *smallest_greater))
                    smallest_greater = i;

        }
    }
}
void permute(char *a, int i, int n)
{
   int j;
   if (i == n)
     printf("%s\n", a);
   else
   {
        for (j = i; j <= n; j++)
        {
          swap((a+i),(a+j));
          permute(a,i+1,n);
          swap((a+i),(a+j)); //backtrack
       }
   }
}
 
/* Driver program to test above functions */
int main()
{
   char a[100000];
   cin>>a;
   int l=strlen(a);
   permute(a, 0, l-1);
   //permute2(a,5);

   //getchar();
   return 0;
}