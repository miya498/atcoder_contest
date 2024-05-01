#include <bits/stdc++.h>
using namespace std;

int main() {
  string S;
  cin >> S;
  int i,ans=1;
  // ここにプログラムを追記
  for(i=1; i<S.size(); i++){
    if(S.at(i)=='+'){
        ans++;
    }else if(S.at(i) == '-'){
        ans--;
    }
  }
  cout << ans << endl;
}
