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
    vector<int> alph(26,0);

    for(int i=0;i<s.size();i++){
        int index=s[i]-'a'; 
        alph[index]++;
    }
    ll sum=0;
    bool dic=false;
    int kazu=0;
    for(int i=0;i<26;i++){
        if(alph[i]>1){
            dic=true;
        }
        sum+=alph[i]*(s.size()-alph[i]);
    }
    ll ans=sum/2;
    if(dic){
        ans++;
    }
    
    cout << ans <<endl;

    return 0;
}
