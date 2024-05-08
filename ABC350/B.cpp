#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int n,q;
    cin >>n >>q;
    vector<int> ans(n,1);
    vector<int> t(q);
    for(int i=0;i<q;i++){
        cin >> t.at(i);
        int index=t.at(i)-1;
        if(ans.at((index))==1){
            ans.at((index))=0;
        }else{
            ans.at((index))=1;
        }    
    }
    int count=0;
    for(int i=0;i<n;i++){
        if(ans.at(i)==1){
            count++;
        }
    }

    cout << count <<endl;
    return 0;
}
