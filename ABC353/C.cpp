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
    vector <ll> a(n);
    ll sum=0;
    for(int i=0;i<n;i++){
        cin >> a[i];
        sum+=a[i];
    }

    ll ans=sum*(n-1);
    int count=0;
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            if((a[i]+a[j])>=100000000){
                count++;
            }
        }
    }
    cout << ans << endl;

    cout << ans-count*100000000 <<endl;
    return 0;
}
