#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int count_overlapping_intervals(const vector<pair<int, int>> &intervals) {
    int n = intervals.size();
    vector<pair<int, int>> events;

    // 各区間の始点と終点をイベントとして追加
    for (int i = 0; i < n; i++) {
        events.emplace_back(intervals[i].first, 1);  // 始点イベント
        events.emplace_back(intervals[i].second + 1, -1); // 終点イベント (+1 で開始イベントとの区別)
    }

    // イベントをソート (時間が同じなら、終了イベントが始点イベントの前に来る)
    sort(events.begin(), events.end());

    int active_intervals = 0;
    int result = 0;

    // スイープラインアルゴリズム
    for (const auto &event : events) {
        active_intervals += event.second;
        if (event.second == 1) {
            // 始点イベントのとき、現在のアクティブな区間の数を結果に加算
            result += (active_intervals - 1); // 自身を除いたアクティブな区間
        }
    }

    return result;
}

int main() {
    int n;
    cin >> n;
    vector<pair<int, int>> intervals(n);
    for (int i = 0; i < n; i++) {
        cin >> intervals[i].first >> intervals[i].second;
    }

    int result = count_overlapping_intervals(intervals);
    cout << result << endl;

    return 0;
}
