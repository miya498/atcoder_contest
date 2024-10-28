#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int n, a, b;
    cin >> n >> a >> b;

    int d;
    int minv = a+b, maxv = 0, minv2 = a+b, maxv2 = 0;
    for(int i=0; i<n; i++){
        cin >> d;
        minv = min(minv, d%(a+b));
        maxv = max(maxv, d%(a+b));
        minv2 = min(minv2, (d+a)%(a+b));
        maxv2 = max(maxv2, (d+a)%(a+b));
    }

    if(maxv-minv<a || maxv2-minv2<a){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }

    return 0;
}
