#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    string s,t;
    cin >> s;
    cin >> t;

    int count=0;
    for(int i=0;i<t.length();i++){
    

        if(s.at(count)==t.at(i) && count==s.length()-1){
            cout << i+1 <<endl;
            break;
        }else if(s.at(count)==t.at(i)){
            cout << i+1 << " ";
            count++;
        }

    }
    
    return 0;
}
