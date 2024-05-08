#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    ll n;
    cin >>n;

    vector <int> a(n),b(n),c(n);
    rep(i,n){
        cin >> a.at(i) >> b.at(i);
        c.at(i)=b.at(i)-a.at(i);
    }

    ll index= distance(c.begin(),max_element(c.begin(),c.end()));
    ll ans=0;
    for(int i=0;i<n;i++){
        if(i == index){
            ans+=b.at(i);
        }else{
            ans+=a.at(i);
        }
    }    
    
    cout << ans <<endl;

    return 0;
}
