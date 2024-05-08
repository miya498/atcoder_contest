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
    for(int i=1;i<=n;i++){
        if(i%3==0){
            cout << 'x';
        }else{
            cout <<'o';
        }
    }
    cout << endl;
    
    return 0;
}
