#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int n,k;
    cin >>n >>k;
    vector <int> a(n);
    for(int i=0;i<n;i++){
        cin >> a[i];
        if(a[i]%k == 0){
            cout << a[i]/k <<" ";
        }
    }
    cout << endl;
    return 0;
}
