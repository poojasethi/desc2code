#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>

#define MAXN 100010
#define INF 0x3F3F3F3F

using namespace std;

int grafo[30][30];
string s1, s2;

int main(){

	int i, j, k, min, n, nv, a, b, sz1, sz2, cost;
	char u, v;

	for( i = 0; i < 30; i++ ){
		for( j = 0; j < 30; j++ )
			grafo[i][j] = INF;
		grafo[i][i] = 0;
	}

	cin >> s1;
	cin >> s2;

	sz1 = s1.size();
	sz2 = s2.size();

	cin >> n;
	while( n-- ){
		cin >> u >> v >> cost;
		if( grafo[u-'a'][v-'a'] > cost ) 
			grafo[u-'a'][v-'a'] = cost; 
	}

	if( sz1 == sz2 ){
		for( k = 0; k < 30; k++ )
			for( i = 0; i < 30; i++ )
				for( j = 0; j < 30; j++ ){
					if( grafo[i][j] > grafo[i][k]+grafo[k][j] )
						grafo[i][j] = grafo[i][k] + grafo[k][j];
				}
		
		cost = 0;
		for( i = 0; i < sz1; i++ ){
			
			a = s1[i]-'a'; b = s2[i]-'a';
			
			min = INF;
			for( j = 0; j < 30; j++ ){
				if( (grafo[a][j] + grafo[b][j]) < min ){
					min = grafo[a][j] + grafo[b][j];
					nv = j;
				}
			}

			if( min == INF ){
				cout << "-1\n"; 
				return 0;
			}
			
			cost += min;
			s1[i] = s2[i] = nv+'a';
		
		}
		cout << cost << endl << s1 << endl;
	} else cout << "-1\n";

	return 0;
}

