#include <cstdio>

int n, m;
char tmp[600010];
struct Trie{
	Trie *next[3];
	bool end;
	Trie()
	{
		for(int i = 0; i < 3; i++) next[i] = 0;
		end = 0;
	}
}*root;

void insert(char *str, Trie *p)
{
	for(int i = 0; str[i]; i++)
	{
		int x = str[i] - 'a';
		if(!p -> next[x]) p -> next[x] = new Trie;
		p = p -> next[x];
	}
	p -> end = 1;
}
bool find(char *str, Trie *p, bool change)
{
	if(!*str) return change && p -> end;
	int x = *str - 'a';
	bool flag = 0;
	for(char ch = 'a'; ch <= 'c'; ch++) if(p -> next[ch - 'a'])
	{
		if(ch == *str) flag |= find(str+1, p -> next[ch - 'a'], change);
		else{
			if(change) continue;
			flag |= find(str+1, p -> next[ch - 'a'], !change);
		}
	}
	return flag;
}

int main()
{
	root = new Trie;
	scanf("%d%d", &n, &m);
	for(int t = 1; t <= n; t++)
	{
		scanf("%s", tmp);
		insert(tmp, root);
	}
	while(m--)
	{
		scanf("%s", tmp);
		puts(find(tmp, root, 0) ? "YES" : "NO");
	}
	return 0;
}
