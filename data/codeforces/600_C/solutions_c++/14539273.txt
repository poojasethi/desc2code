#include <bits/stdc++.h>

using namespace std;

char s[200000];

int nletter[26];

int main() {
	scanf("%s", s);
	int len = strlen(s);
	for(int i=0; i<len; i++)
		nletter[s[i] - 'a']++;
	int i=0, j=len-1;
	for(int i=0, j=26-1; i<j; i++) {
		if(nletter[i] % 2 == 0)
			continue;
		while(nletter[j] % 2 == 0 && j > i) j--;
		if(j <= i)
			break;
		nletter[i]++;
		nletter[j]--;
	}
	for(int i=0; i<26; i++)
		for(int j=0; j<nletter[i]/2; j++)
			putchar('a'+i);

	for(int i=0; i<26; i++)
		if(nletter[i]%2 == 1)
			putchar('a'+i);

	for(int i=25; i>=0; i--)
		for(int j=0; j<nletter[i]/2; j++)
			putchar('a'+i);
	putchar('\n');
	return 0;
}
