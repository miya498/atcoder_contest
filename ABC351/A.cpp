#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    
    vector <int> a(9);
    int sum_a=0;
    for(int i=0;i<9;i++){
        cin >> a.at(i);
        sum_a+=a.at(i);
    }
    vector <int> b(8);
    int sum_b=0;
    for(int i=0;i<8;i++){
        cin >> b.at(i);
        sum_b+=b.at(i);
    }
    int ans;
    ans=sum_a+1-sum_b;

    cout << ans <<endl;
    return 0;
}
