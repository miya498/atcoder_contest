#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    string s;
    cin >>s;
    int count=0;
    for(int i=0;i<3;i++){
        if(s.at(i)== '1'){
            count++;
        }
    }

    cout << count << endl;
    return 0;
}
