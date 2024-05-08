#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    string s;
    cin >>s;
    set<string> st;
    for(int i=0;i<s.length();i++){
        for(int j=1; i+j <= s.length();j++){
            st.insert(s.substr(i,j));
        }
    }

    cout << st.size() <<endl;

    // set内の要素を表示
    /*
    for (auto it = st.begin(); it != st.end(); ++it) {
        cout << *it << endl;
    }
    */
    return 0;
}
