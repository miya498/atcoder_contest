#include <iostream>
#define MOD 998244353

using namespace std;

int popcount(int x) {
    int count = 0;
    while (x) {
        count += x & 1;
        x >>= 1;
    }
    return count;
}

int main() {
    long long  N, M;
    cin >> N >> M;
    
    long long result = 0;
    
    for (long k = 0; k <= N; ++k) {
        result = (result + popcount(k & M)) % MOD;
    }
    
    cout << result << endl;
    return 0;
}
