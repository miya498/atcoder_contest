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
    string t;
    cin >>t;
    transform(t.begin(), t.end(), t.begin(), ::tolower);


    int j=0;
    if(t.at(2)=='x'){
        rep(i,s.length()){
            if(s.at(i)==t.at(j)){
                j++;
            }
            if(j==2) break;
        }
        if(j==2){
            cout << "Yes" << endl;
        }else{
            cout << "No" << endl;
        }
    }else{
        rep(i,s.length()){
            if(s.at(i)==t.at(j)){
                j++;
            }
            if(j==3)  break;
        }
        if(j==3){
            cout << "Yes" << endl;
        }else{
            cout << "No" << endl;
        }
    }    
    return 0;
}
