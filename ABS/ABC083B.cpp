#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int sum_keta(int n){
    int sum=0;
    while(n>0){
        sum+=n%10;
        n/=10;
    }
    return sum;
}

int main(){
    int n,a,b;
    cin >>n >>a >>b;
    int ans=0;
    for(int i=1;i<=n;i++){
        int sum = sum_keta(i);
        if((a <= sum) && (sum <= b )){
            /* cout << count <<endl;*/
            ans+=i;
        }        
    }
    cout << ans <<endl;
    return 0;
}
