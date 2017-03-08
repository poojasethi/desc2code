#include <iostream>
#include <string>
#include <vector>
using namespace std;

int n, m;
string card;
int j1x = 20, j1y = 20;
int j2x = 20, j2y = 20;
int sq1x = 20, sq1y = 20;
int sq2x = 20, sq2y = 20;

vector<vector<int> >field(50);

string suits = "HCDS";
string faces = "AT23456789JQK";

void input() {
	cin>>n>>m;
	for(int x=0; x<30; ++x) {
		field[x].resize(30);
	}

	for(int x=0; x<n; ++x) {
		for(int y=0; y<m; ++y) {
			cin>>card;
			int i, j;
			if (card[0] == 'J') {
				if (card[1] == '1' || card[1] == '2') {
					if (card[1] == '1') {
						j1x = x;
						j1y = y;
					} else {
						j2x = x;
						j2y = y;
					}
					continue;
				}
			}

			for(i=0; i < 13; ++i) {
				if (card[0] == faces[i]) {
					break;
				}
			}
			for(j=0; j < 13; ++j) {
				if (card[1] == suits[j]) {
					break;
				}
			}
			field[x][y] = j*13 + i;
		}
	}
}

bool check() {
	int squares_found = 0;

	bool used[52] = {false};
	for(int x = 0; x < n; ++x) {
		for(int y = 0; y < m; ++y) {
			int code = field[x][y];
			if (used[code]) {
				return false;
			}
			used[code] = true;
		}
	}

	for(int x = 0; x + 2 < n; ++x) {
		for(int y = 0; y + 2 < m; ++y) {
			int suits[4] = {0};
			int faces[13] = {0};
			for(int i=0;i<3;++i) {
				for(int j=0;j<3;++j) {
					++suits[field[x+i][y+j] / 13];
					++faces[field[x+i][y+j] % 13];
				}
			}
			bool suit_valid = true;
			for(int f=0; f<4;++f) {
				if (suits[f] != 0 && suits[f] != 9) {
					suit_valid = false;
					break;
				}
			}
			bool faces_valid = true;
			for(int f=0; f<13;++f) {
				if (faces[f] > 1) {
					faces_valid = false;
					break;
				}
			}
			if (suit_valid || faces_valid) {
				++squares_found;
				if (squares_found == 1) {
					sq1x = x+1;
					sq1y = y+1;
				}
				if (squares_found == 2) {
					sq2x = x+1;
					sq2y = y+1;
					bool x_overlap = (sq2x >= sq1x && sq2x <= sq1x + 2) || (sq1x >= sq2x && sq1x <= sq2x + 2);
					bool y_overlap = (sq2y >= sq1y && sq2y <= sq1y + 2) || (sq1y >= sq2y && sq1y <= sq2y + 2);
					if (x_overlap && y_overlap) {
						squares_found -= 1;
						sq2x = -1;
						sq2y = -1;
					} else {
						return true;
					}
				}
			}
		}
	}

	return false;
}

string card_name(int i) {
	int suit = i / 13;
	int face = i % 13;
	string s;
	s += faces[face];
	s += suits[suit];
	return s;
}

void solve() {
	for(int i = 0; i < 52; ++i) {
		field[j1x][j1y] = i;
		for(int j = 0; j < 52; ++j) {
			field[j2x][j2y] = j;
			if (check()) {
				cout<<"Solution exists."<<endl;
				if (j1x == 20 && j2x == 20) {
					cout<<"There are no jokers."<<endl;
				} else if (j1x != 20 && j2x != 20) {
					cout<<"Replace J1 with "<<card_name(i)<<" and J2 with "<<card_name(j)<<"."<<endl;
				} else if (j1x != 20) {
					cout<<"Replace J1 with "<<card_name(i)<<"."<<endl;
				} else {
					cout<<"Replace J2 with "<<card_name(j)<<"."<<endl;
				}
				cout<<"Put the first square to ("<<sq1x<<", "<<sq1y<<")."<<endl;
				cout<<"Put the second square to ("<<sq2x<<", "<<sq2y<<")."<<endl;
				return;
			}
		}
	}
	cout<<"No solution."<<endl;
}

int main() {
	//freopen("d.in","rt", stdin);
	input();
	solve();
	return 0;
}