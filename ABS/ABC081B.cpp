#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int N;
    cin >>N;
    vector<int> data(N);
    for(int i=0;i<N;i++){
        cin >>data.at(i);        
    }
    int count=-1;
    bool det=true;

    while(det){
        for(int i=0;i<N;i++){
            if((data.at(i)%2)==1){
                det = false;
            }
            data.at(i)=data.at(i)/2; 
        }
        count++;
    }
    cout << count <<endl;
    return 0;
}
