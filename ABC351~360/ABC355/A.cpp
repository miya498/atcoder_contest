#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int a,b;
    cin >>a >>b;
  
    if(a == b){
        cout << -1 << endl;
    }else{
        if(a==1 && b==2){
            cout << 3 << endl;
        }else if(a==2 && b==1){
            cout << 3 << endl;            
        }else if(a==1 && b==3){
            cout << 2 << endl; 
        }else if(a==3 && b==1){
            cout << 2 << endl; 
        }else if(a==2 && b==3){
            cout << 1 << endl; 
        }else if(a==3 && b==2){
            cout << 1 << endl; 
        }
    }
    
    return 0;
}
