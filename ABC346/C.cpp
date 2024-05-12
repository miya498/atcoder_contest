#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int n;
    ll k;
    cin >>n >>k;
    ll a;
    set<int> b;
    
    for(int i=0;i<n;i++){
        cin >> a;
        if(a<=k)    b.insert(a);
    }
    ll ans=k*(k+1)/2;
    
    for(auto itr=b.begin();itr != b.end();itr++){
        ans-=*itr;
    }
    cout << ans <<endl;
    return 0;
}
