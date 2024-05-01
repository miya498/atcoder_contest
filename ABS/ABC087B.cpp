#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int A;
    cin >>A;
    int B;
    cin >>B;
    int C;
    cin >>C;
    int X;
    cin >>X;
    int sum,ans=0;
    for(int i=0;i<=A;i++){
        for(int j=0;j<=B;j++){
            for(int k=0;k<=C;k++){
                sum=500*i+100*j+50*k;
                if(sum==X){
                    ans++;
                }
            }
        }
    }
    cout << ans <<endl;
    return 0;
}
