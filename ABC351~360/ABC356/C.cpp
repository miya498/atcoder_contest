#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

int main() {
    int N, M, K;
    cin >> N >> M >> K;
    
    vector<vector<int>> tests(M);
    vector<char> results(M);
    
    for (int i = 0; i < M; ++i) {
        int C;
        cin >> C;
        tests[i].resize(C);
        for (int j = 0; j < C; ++j) {
            cin >> tests[i][j];
            --tests[i][j]; 
        }
        cin >> results[i];
    }
    
    int valid_combinations = 0;
    int total_combinations = 1 << N; 
    
    for (int comb = 0; comb < total_combinations; ++comb) {
        bool is_valid = true;
        for (int i = 0; i < M; ++i) {
            int count = 0;
            for (int key : tests[i]) {
                if (comb & (1 << key)) {
                    ++count;
                }
            }
            if ((results[i] == 'o' && count < K) || (results[i] == 'x' && count >= K)) {
                is_valid = false;
                break;
            }
        }
        if (is_valid) {
            ++valid_combinations;
        }
    }
    
    cout << valid_combinations << endl;
    return 0;
}
