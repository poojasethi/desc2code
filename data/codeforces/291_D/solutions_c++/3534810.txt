#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int n, k;
int main(int argc, char** argv) {
    scanf("%d%d", &n, &k);
    int d = 1;
    for(int j = 0; j < k; ++j){
        for(int i = 1; i < n; ++i){
            int id = i + d;
            id = id > n ? n : id;
            printf("%d ", id);
        }
        printf("%d\n", n);
        d <<= 1;
    }
    return 0;
}

