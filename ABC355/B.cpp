#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll = long long;
using P = pair<int, int>;

bool has_consecutive_elements_from_A(vector<int> &A, vector<int> &B) {
    // A と B を結合してソート
    vector<int> C;
    C.reserve(A.size() + B.size());
    C.insert(C.end(), A.begin(), A.end());
    C.insert(C.end(), B.begin(), B.end());
    sort(C.begin(), C.end());
    
    // 連続する A の要素をチェック
    unordered_set<int> A_set(A.begin(), A.end());
    for (size_t i = 0; i < C.size() - 1; i++) {
        if (A_set.count(C[i]) && A_set.count(C[i + 1])) {
            return true;
        }
    }
    return false;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    vector<int> b(m);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }

    if (has_consecutive_elements_from_A(a, b)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}
