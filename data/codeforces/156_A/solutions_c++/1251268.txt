#include <stdio.h>
#include <string.h>

int main() {
	char s[6001], t[2001];
	gets(s); gets(t);



	int sn = strlen(s), tn = strlen(t), m = tn;
	for (int i = -tn; i <= sn; i++) {
		int c = 0;
		for (int j = 0; j < tn; j++)
			if (i+j < 0 || i+j >= sn || s[i+j] != t[j])
				c++;

		if (c < m)
			m = c;
	}

	printf("%d\n", m);

	return 0;
}
