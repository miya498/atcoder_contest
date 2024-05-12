#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    ll x;
    cin >>x;
    ll ans;
    if(x >= 0){
        ans=(x+9)/10;
    }else{
        ans=x/10;
    }
    
    cout << ans <<endl;
    return 0;
}