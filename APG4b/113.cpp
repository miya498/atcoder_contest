#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> point(N);
  for(int i=0; i<N;i++){
    cin >> point.at(i);
  } 

  int count=0,ave;
  for(int i=0;i<N;i++){
    count+=point.at(i);
  }

  ave=count/N;
  for(int i=0;i<N;i++){
    if(point.at(i)>=ave){
        cout << point.at(i)-ave << endl;
    }else{
        cout << ave-point.at(i) << endl;
    }
  }



}
