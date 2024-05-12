#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int w,b;
    cin >> w >> b;
    string S="wbwbwwbwbwbw";
    string t="";
    rep(i,20){
        t+=S;
    }
    bool ans=false;
    for(int i=0;i<12;i++){
        int count_w=0;
        int count_b=0;
        for(int j=0;j<w+b;j++){
            if(t[i+j] == 'w'){
                count_w++;
            }else{
                count_b++;
            }
        }
        if(count_w==w && count_b==b){
            ans=true;
            break;
        }
    }

    if(ans){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}
