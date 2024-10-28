#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int N,L,R,c;
    cin >>N >> L >> R;
    vector <int> v(N);
    for(int i=0;i<N;i++){
        v[i]=i+1;
    }
    
    reverse(v.begin() + L - 1, v.begin() + R);
    

    for(int i=0;i<N;i++){
        cout << v[i] <<" ";
    }
    cout <<endl;
    return 0;
}
