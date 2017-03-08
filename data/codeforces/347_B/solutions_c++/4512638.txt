# include <stdio.h>

int n, k,ans;

int T[100009], a;

int main()
{
	scanf("%d",&n);
	
	for(int h=1; h<=n; h++)
	{
		scanf("%d",&a);
		
		a++;
		
		if(a != h)	T[h] = a;
		
		else 	ans++;
	}
	
	for(int h=1; h<=n; h++)
		if(T[h]  &&  T[T[h]] == h)	k = 1;
	
	printf("%d\n",ans+(ans != n ? 1 : 0)+k);
}
