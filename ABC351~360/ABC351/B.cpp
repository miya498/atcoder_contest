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
    vector <vector<char>> a(n,vector<char>(n));
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin >> a.at(i).at(j);
        }
    }

    vector <vector<char>> b(n,vector<char>(n));
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin >> b.at(i).at(j);
        }
    }

    int ans_i,ans_j;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(a.at(i).at(j)!=b.at(i).at(j)){
                ans_i=i+1;
                ans_j=j+1;
            }
        }
    }
    cout << ans_i <<' '<< ans_j<<endl;
    return 0;
}
