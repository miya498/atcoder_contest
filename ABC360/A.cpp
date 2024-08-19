#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main() {
    string input;
    cin >> input;

    size_t posR = input.find('R');
    size_t posM = input.find('M');

    cout << ((posR != string::npos && posM != string::npos && posR < posM) ? "Yes" : "No") << endl;

    return 0;
}
