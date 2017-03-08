#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

int main() {
    LL n;
    cin >>n;
    cin.ignore();
    int num = 0;
    string msg = "";
    string ret = "Unhandled Exception";
    for (int i=0;i<n;i++) {
        string s;
        getline(cin, s);

        int i = 0;
        while (s[i] == ' ') i++;

        /* try */
        if (s[i] == 't' and s[i+1] == 'r') {
            if (msg != "") num++;
        }

        /* throw */
        else if (s[i] == 't') {
            i += 5;
            while (s[i] == ' ' or s[i] == '(') i++;
            while (s[i] != ' ' and s[i] != ')') msg += s[i++];
        }

        /* catch */
        else if (s[i] == 'c') {
            if (0 < num) {
                num--;
                continue;
            }
            i += 5;
            string msg1 = "";
            while (s[i] == ' ' or s[i] == '(') i++;
            while (s[i] != ' ' and s[i] != ',') msg1 += s[i++];
            if (msg != msg1) continue;
            while (s[i] != '"') i++;
            i++;
            ret = "";
            while (s[i] != '"') ret += s[i++];
            break;
        }
    }

    cout <<ret <<endl;
    return 0;
}
