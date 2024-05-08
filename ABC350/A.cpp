#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    string S;
    cin >>S;
    string T=S.substr(3);
    int dict = stoi(T);
    
    if(1 <= dict && dict <=349 && dict !=316){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}
