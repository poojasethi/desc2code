#include <iostream>

using namespace std;

/* at most one element in array gives different reminder % (k + 1)*/
int main() {
	int T, n, k, l;
	int x;
	cin >> T;

	for (int t = 0; t < T; ++t) {
		cin >> n >> k;
		int reminders[10] = {0};
		bool pos = true;

		for (int i = 0; i < n; ++i) {
			cin >> l;
			reminders[(l % (k + 1))] += 1;
		}

		int first = -1, second = -1;
		//cout << endl;
		for (int i = 0; i < 10; ++i) {
			//cout << i << " : " << reminders[i] << ", ";
			if (reminders[i] == 0)	continue;
			if (first == -1)	first = i;
			else if (second == -1)	second = i;
			else			pos = false;
		}
	
		//cout << "\nfirst : " << first << ", reminder = " << reminders[first] << "\n second : " << second << ", reminders = " << reminders[second] << endl;

		/* there are more than one reminders, then one of them must be 1 */
		if (second != -1 && reminders[first] != 1 && reminders[second] != 1)
			pos = false;

		if (pos)
			cout << "YES\n";
		else
			cout << "NO\n";
	}

	return 0;
}
