#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int n,x,y,z;
    int a,b;
    cin >>n >> x >> y >> z;
    
    if(x > y){
        a = y;
        b = x;
    }else{
        a=x;
        b=y;
    }
    
    if(a <= z && z <=b){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
    return 0;
}
