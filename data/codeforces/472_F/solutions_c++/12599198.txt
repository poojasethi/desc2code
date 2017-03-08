#include <cstdio>
#include <vector>

using namespace std;

const int N = 10100;
const int X = 31;

int A[N],B[N],n;

class node {
public:
    int x,y;
    node(){}
    node(int x, int y):x(x),y(y){}
};

vector<node> opa,opb;

void perform_an_operation(int x, int y, vector<node> &op, int arr[]) {
    op.push_back(node(x,y));
    arr[x]^=arr[y];
}

void do_gauss(int arr[], vector<node> &op) {
    int nr = 0;
    for (int i=0; i<X; i++) {
        for (int j=nr; j<n; j++) {
            if (arr[j]&(1<<i)) {
                if (j != nr) {
                    perform_an_operation(nr,j,op,arr);
                    perform_an_operation(j,nr,op,arr);
                    perform_an_operation(nr,j,op,arr);
                }
                for (int k=0; k<n; k++) {
                    if (k != nr) {
                        if ((1<<i)&arr[k]) {
                            perform_an_operation(k,nr,op,arr);
                        }
                    }
                }
                nr++;
                break;
            }
        }
    }
}

int main() {
    while(scanf("%d",&n)+1) {
        opa.clear();
        opb.clear();
        for (int i=0; i<n; i++) {
            scanf("%d",&A[i]);
        }
        for (int i=0; i<n; i++) {
            scanf("%d",&B[i]);
        }
        do_gauss(A,opa);
        do_gauss(B,opb);
        int k = 0;
        for (int i=0; i<X; i++) {
            for(;(A[i]&(1<<k)) == 0 && k<X;) {
                k++;
            }
            for (int j=0; j<X&&j<n; j++) {
                if ((A[j]^B[j])&(1<<k)) {
                    perform_an_operation(j,i,opa,A);
                }
            }
        }
        for (int i=0; i<n; i++) {
            if (A[i] != B[i]) {
                puts("-1");
                return 0;
            }
        }
        printf("%d\n",opa.size()+opb.size());
        for (int i=0; i<opa.size(); i++) {
            printf("%d %d\n",opa[i].x+1,opa[i].y+1);
        }
        for (int i=opb.size()-1; i>=0; i--) {
            printf("%d %d\n",opb[i].x+1,opb[i].y+1);
        }
    }
    return 0;
}
