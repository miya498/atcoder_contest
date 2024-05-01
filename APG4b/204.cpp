#include <bits/stdc++.h>
using namespace std;

int main() {
  // A君の回答を受け取る
  vector<vector<int>> A(9, vector<int>(9));
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      cin >> A.at(i).at(j);
    }
  }

  int correct_count = 0; // ここに正しい値のマスの個数を入れる
  int wrong_count = 0;   // ここに誤った値のマスの個数を入れる
  int ans;
  // 正しく修正した表を出力
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 9; j++) {
      ans = (i+1)*(j+1);
      cout << ans;
      if(ans == A.at(i).at(j)){
        correct_count++;
      }else{
        wrong_count++;
      }
      if (j < 8){
        cout << " ";
      }else{
        cout << endl;
      }
    }
  }
  // 正しいマスの個数を出力
  cout << correct_count << endl;
  // 誤っているマスの個数を出力
  cout << wrong_count << endl;
}
