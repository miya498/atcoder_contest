#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main() {
    string S, T;
    cin >> S;
    cin >> T;

    int lenS = S.length();
    int lenT = T.length();
    bool found = false;

    for (int w = 1; w < lenS && !found; ++w) {
        for (int c = 1; c <= w; ++c) {
            string a;
            for (size_t i = 0; i + c <= S.size(); i += w) {
                a += S[i + c - 1];
            }
            if (a == T) {
                found = true;
                break;
            }
        }
    }

    if(found){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }

    return 0;
}
