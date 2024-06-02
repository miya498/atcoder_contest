#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int n;
    cin >>n;
    vector <string> s(n);
    vector <int> c(n);
    int rate=0;
    for(int i=0;i<n;i++){
        cin >> s[i] >> c[i];
        rate+=c[i];
    }

    string tmp;
    for (int i = 0; i < n-1; ++i) {
        for (int j = 0; j < n-1; ++j) {
            if (s[j] > s[j+1]) {
                tmp = s[j];
                s[j] = s[j+1];
                s[j+1] = tmp;
            }
        }
    }

    int ans=rate%n;

    cout << s[ans] <<endl;
    
    return 0;
}
