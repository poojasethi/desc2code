#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long int ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

int countSteps(int a, int b, int c){
	int x = a, y = 0, temp;
	int moves = 1;
	while(x != c && y!=c){
		temp = min(x, b-y);
		x -= temp;
		y += temp;
		moves++;
		if(x == c || y == c)
			break;
		if(x == 0){
			x = a;
			moves++;
		}
		if(y == b){
			y = 0;
			moves++;
		}	
	}
	return moves;
}

int main(){
	ios::sync_with_stdio(false);
	int n,x,y,a,b,c; cin >> n;
	while(n--){
		cin >> x >> y >> c;
		a = min(x,y); b = max(x,y);
		if(c > b){
			cout << "-1" << endl;
			continue;
		}
		if(c % __gcd(a,b) != 0){
			cout << "-1" << endl;
			continue;
		}
		if(c==a || c==b){
			cout << 1 << endl;
			continue;
		}
		cout << min(countSteps(a,b,c), countSteps(b,a,c)) << endl;
	}
	return 0;
}