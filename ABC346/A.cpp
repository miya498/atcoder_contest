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
    vector <int> a(n);
    for(int i=0;i<n;i++){
        cin >> a[i];
    }
    
    for(int i=0;i<n-1;i++){
        int b= a[i]*a[i+1];
        cout << b << " ";
    }
    cout << endl;
    return 0;
}
