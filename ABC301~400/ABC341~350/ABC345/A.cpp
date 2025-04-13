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
    bool ans=false;
    bool dic=true;
    int end=s.length()-1;
    if(s[0] == '<' && s[end] == '>'){
        for(int i=1;i<end;i++){
            if(s[i]!='='){
                dic=false;
                break;
            }
        }
        if(dic != false){
            ans = true;
        }
    }
    
    if(ans){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}
