#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int n,m;
    cin >>n >>m;
    vector <int> a(m);
    vector <int> ans(m);
    vector<vector<int>> data(n, vector<int>(m));
    for(int i=0;i<m;i++){
        cin >> a[i];
        ans[i]=0;
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
        cin >> data[i][j];
        ans[j]+=data[i][j];
        }
    }
    bool res=true;
    for(int i=0;i<m;i++){
        if(a[i]>ans[i]){
            res =false;
            break;
        }
    }
    if(res){
        cout << "Yes" <<endl;
    }else{
        cout << "No" <<endl;
    }
    return 0;
}