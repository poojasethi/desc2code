/* bhupkas */

#include "stdio.h"
#include "iostream"
#include "string.h"
#include "string"

using namespace std;

#define FOR(i,a,b)		for(i=a;i<b;i++)

char s[200005];
int N,K;

int getMinimumPaints()
	{
    		if(K > N)	return -1;
		int cc = 0, ans=0,j,i, mx = 0;
		FOR(i, 0, N)
			{
				cc = 0;
				for(j = i; s[j] == s[i] && s[j]; j++)	cc++;
				mx = max(mx, cc);
				ans += (cc - 1) / K + 1;
				i += cc - 1;
			}
 
		if(K > mx)	return -1;
		return ans;
	}
 
int main(){
    int T;
    cin >> T;
    while(T--)
    	{
		cin >> N >> K;
		getchar();
		scanf("%s",s);
		cout << getMinimumPaints() << endl;
	}
    return 0;
} 
