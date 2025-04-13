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
    vector <int> alpha(26,0);
    
    rep(i,s.length()){
        alpha.at((s.at(i))-'a')++;   
    }

    vector <int> freq(101,0);
    rep(i,26){
        freq.at(alpha.at(i))++;
    }
    bool ans = true;

    for(int i=1;i<101;i++){
        if(freq.at(i) != 0 && freq.at(i) != 2){
            ans = false;
            break;
        }
    }


    if(ans){
        cout << "Yes" << endl;
    }else{
        cout << "No" <<endl;
    }
    return 0;
}
