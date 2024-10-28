#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

#include <vector>

using namespace std;

int main(){
    int n;
    cin >>n;
    vector <int> a(n);
    vector <int> copy(0);
    for(int i=0;i<n;i++){
        cin >> a.at(i);
    }

    int num;

    for(int i=0;i<n;i++){
        num = a.at(i);
        copy.push_back(num);
        for(int j=0;j>-1;j++){
            int size=copy.size();
            if(size==1){
                break;
            }else if(copy.at(size - 1) != copy.at(size - 2)){
                break;
            }else{
                int ball = copy.at(size - 1) + 1;
                copy.pop_back();
                copy.pop_back();
                copy.push_back(ball);
            } 
        }        
    }
    cout << copy.size() <<endl;
    return 0;
}
