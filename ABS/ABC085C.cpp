#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
#define rep(i,n) for (int i=0;i<(int)(n);i++)
using ll=long long;
using P=pair<int,int>;

int main(){
    int n,y;
    cin >>n >>y;
    /*vector <int> v(n,d);*/
    int sum;
    bool check=false;
    /*n=10000*i+5000*j+1000*(n-i-j)
      n=9000*i+4000*j+1000n 
    */
    for(int i=0;i<=n;i++){
        for(int j=0;j<=n;j++){
            if((n-i-j)<0) break;
            sum =j*9000+i*4000+n*1000;
            if(sum==y){
                check = true;
                cout << j << " "<<i <<" " <<n-i-j << endl; 
            }
            
        }
        if(check == true){
            break;
        }
    }
    
   
    if(check == false){
        cout << -1 <<" " << -1 << " " <<-1<<endl;
    }
    
}
