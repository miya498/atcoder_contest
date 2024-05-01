#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){

    vector <string> divide={"dream","dreamer","erase","eraser"};

    string S;
    cin >>S;

    reverse(S.begin(),S.end());

    for(int i=0;i<4;i++){
        reverse(divide.at(i).begin(),divide.at(i).end());
    }


    bool ans = true;

    for(int i=0;i<S.size();){
        bool can=false;
        for(int j=0;j<4;j++){
            string d=divide.at(j);
            if(S.substr(i,d.size()) == d){
                can =true;
                i+=d.size();                
            }
            
        }
        if(can == false){
            ans = false;
            break;
        }
    }
    if(ans == true){
        cout<<"YES"<<endl;
    }else{
        cout<<"NO"<<endl;
    }
    
    return 0;
}
