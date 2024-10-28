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
    vector <int> x(n);
    vector <int> y(n);
    for(int i=0;i<n;i++){
        cin >> x.at(i) >>y.at(i);
    }
    
    rep(i,n){
        double max=0.0;
        int index =0;
        rep(j,n){
            if(j==i){
                continue;
            } 
            double d=sqrt(pow(x.at(i)-x.at(j),2)+pow(y.at(i)-y.at(j),2));
            if(max < d){
                max = d;
                index = j;
            }
            }
        cout << index+1 << endl;
        }
        return 0;
}
 
    
