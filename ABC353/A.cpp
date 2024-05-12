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
    vector <int> h(n);
    for(int i=0;i<n;i++){
        cin >> h[i];
    }
    int ans=-1;
    rep(i,n){
        if(h[i]>h[0]){
            ans=i+1;
            break;
        }
    }
    cout << ans <<endl;
    return 0;
}
