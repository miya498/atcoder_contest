#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, T;
    cin >> N >> T;
    vector<int> A(T);
    for (int i = 0; i < T; i++) {
        cin >> A[i];
    }

    // 行と列のカウント
    vector<int> rowCount(N, 0);
    vector<int> colCount(N, 0);
    int mainDiagCount = 0;
    int antiDiagCount = 0;
    
    // ビンゴの達成をチェック
    set<int> markedCells;
    for (int t = 0; t < T; t++) {
        int a = A[t];
        int r = (a - 1) / N;  // 行番号 (0-indexed)
        int c = (a - 1) % N;  // 列番号 (0-indexed)

        // すでにマークされている場合はスキップ
        if (markedCells.count(a)) continue;
        markedCells.insert(a);

        rowCount[r]++;
        colCount[c]++;
        if (r == c) {
            mainDiagCount++;
        }
        if (r + c == N - 1) {
            antiDiagCount++;
        }

        // ビンゴ達成チェック
        if (rowCount[r] == N || colCount[c] == N || mainDiagCount == N || antiDiagCount == N) {
            cout << t + 1 << endl;
            return 0;
        }
    }

    // ビンゴが達成されなかった場合
    cout << -1 << endl;
    return 0;
}
