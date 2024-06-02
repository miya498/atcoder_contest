#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int h;
    cin >>h;
    for(int i=1;i<36;i++){
        if((pow(2,i)-1) > h){
            cout << i <<endl;
            break;
        }  
    }
}
