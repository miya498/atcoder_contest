#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N + 1), W(N + 1);
    for (int i = 1; i <= N; ++i) {
        cin >> A[i];
    }
    for (int i = 1; i <= N; ++i) {
        cin >> W[i];
    }

    vector<bool> visited(N + 1, false);
    int totalCost = 0;

    for (int i = 1; i <= N; ++i) {
        if (!visited[i]) {
            int cycleWeightSum = 0;
            int cycleMinWeight = INT_MAX;
            int cycleLength = 0;

            int current = i;
            while (!visited[current]) {
                visited[current] = true;
                cycleWeightSum += W[current];
                cycleMinWeight = min(cycleMinWeight, W[current]);
                current = A[current];
                ++cycleLength;
            }

            totalCost += cycleWeightSum + (cycleLength - 1) * cycleMinWeight;
        }
    }

    cout << totalCost << endl;
    return 0;
}
