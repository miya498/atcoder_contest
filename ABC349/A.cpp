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
    int ans=0;
    vector <int> a(n-1);
    for(int i=0;i<n-1;i++){
        cin >> a.at(i);
        ans+=a.at(i);
    }
    cout <<  -ans <<endl;
    return 0;
}
