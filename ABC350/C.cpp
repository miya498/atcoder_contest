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

    vector <int> a(n),where(n);
    vector<vector<int>> ans(n, vector<int>(2));

    rep(i,n){
        cin >> a.at(i);
        a.at(i)--;
        where.at(a.at(i))=i;
    }    
    
    int count=0;
    rep(i,n-1){
        if(a.at(i)==i){
            continue;
        }
        int j=where.at(i);

        ans.at(count).at(0)= i+1;
        ans.at(count).at(1)= j+1;
        swap(where.at(a.at(i)),where.at(a.at(j)));
        swap(a.at(i),a.at(j));
        count++;
        
    }
    cout << count <<endl;
    rep(i,count){
        cout << ans.at(i).at(0) <<" " << ans.at(i).at(1) <<endl;
    }
    return 0;
}
