#include<limits.h>
#include<math.h> 
#include <stdio.h>
#include<stdlib.h>
#include<string.h>
int main() 
{
    long t,n;
    scanf("%ld",&t);
    while(t--)
    {
        scanf("%ld",&n);
        if(n%3==0 || n%2==0)
        printf("YES\n");
        else 
        printf("NO\n");
    }
	return 0;
}
 