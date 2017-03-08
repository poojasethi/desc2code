#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

const int maxn = 1000 + 10;

int n, m;
int sx, sy, tx, ty;
char s[maxn][maxn];

bool vis[maxn][maxn][4];

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, 1, 0, -1 };

struct Node
{
	int x, y, angle, steps;
	Node() {}
	Node(int x, int y, int a, int s): x(x), y(y), angle(a), steps(s) {}
};

bool in(int x, int y) { return 0<=x && x<n && 0<=y && y<m; }

queue<Node> Q;

int code(char c) {
	if(c == '+') return 15;
	if(c == '-') return 10;
	if(c == '|') return  5;
	if(c == '^') return  1;
	if(c == '>') return  2;
	if(c == '<') return  8;
	if(c == 'v') return  4;
	if(c == 'L') return  7;
	if(c == 'R') return 13;
	if(c == 'U') return 14;
	if(c == 'D') return 11;
	return 0;
}

int rotate(int& x, int angle) {
	while(angle--) {
		x <<= 1;
		if(x >= 16) x -= 15;
	}
}

bool check(int x, int y, int dir, int angle) {
	int code1 = code(s[x][y]);
	rotate(code1, angle);
	int code2 = code(s[x + dx[dir]][y + dy[dir]]);
	rotate(code2, angle);
	return ((code1>>dir)&1) && ((code2>>(dir^2))&1);
}

int BFS() {
	Q.push(Node(sx, sy, 0, 0));
	vis[sx][sy][0] = true;
	while(!Q.empty()) {
		Node t = Q.front(); Q.pop();
		if(t.x == tx && t.y == ty) return t.steps;
		for(int i = 0; i < 4; i++) {
			int nx = t.x + dx[i];
			int ny = t.y + dy[i];
			if(!in(nx, ny) || s[nx][ny] == '*' || vis[nx][ny][t.angle]) continue;
			if(!check(t.x, t.y, i, t.angle)) continue;
			Q.push(Node(nx, ny, t.angle, t.steps + 1));
			vis[nx][ny][t.angle] = true;
		}
		t.angle++; if(t.angle == 4) t.angle = 0;
		if(vis[t.x][t.y][t.angle]) continue;
		t.steps++;
		Q.push(Node(t));

	}
	return -1;
}

int main()
{
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; i++) scanf("%s", s[i]);
	scanf("%d%d%d%d", &sx, &sy, &tx, &ty);
	sx--; sy--; tx--; ty--;
	printf("%d\n", BFS());

	return 0;
}
