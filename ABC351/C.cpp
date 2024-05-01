#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

#include <vector>

using namespace std;

vector<ll> merge_ball(vector<ll> a, int size) {
    if(size <= 1) {
        return a;
    } else if(a.at(size - 1) != a.at(size - 2)) {
        return a;
    } else{
        ll ball = a.at(size - 1) + 1;
        a.pop_back();
        a.pop_back();
        a.push_back(ball);
        return merge_ball(a, size - 1); 
    }
}

int main(){
    int n;
    cin >>n;
    vector <ll> a(n);
    for(int i=0;i<n;i++){
        cin >> a.at(i);
    }

    vector <ll> copy(0);
    ll num;

    for(int i=0;i<n;i++){
        num = a.at(i);
        copy.push_back(num);
        copy = merge_ball(copy,copy.size());
        /*cout << copy.size() <<endl;    */        
    }
    cout << copy.size() <<endl;
    return 0;
}
