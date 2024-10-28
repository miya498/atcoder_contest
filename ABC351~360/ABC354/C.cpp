#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Card {
    int index;
    int strength;
    int cost;
};

bool compareCards(const Card &a, const Card &b) {
    if (a.strength == b.strength) {
        return a.cost > b.cost;
    }
    return a.strength < b.strength;
}

int main() {
    int n;
    cin >> n;

    vector<Card> cards(n);
    for (int i = 0; i < n; ++i) {
        cin >> cards[i].strength >> cards[i].cost;
        cards[i].index = i + 1;
    }

    sort(cards.begin(), cards.end(), compareCards);

    vector <int> result;

    for (int i=1;i<n;i++) {
        if (cards[i].cost > cards[i-1].cost) {
            result.push_back(cards[i-1].index);
        }
    }
    if(cards[n].strength!=cards[n-1].strength){
        result.push_back(cards[n-1].index);
    }else if(cards[n].strength!=cards[n-1].strength && cards[n].cost < cards[n-1].cost){
        result.push_back(cards[n-1].index);
    }

    sort(result.begin(),result.end());

    cout << result.size() << endl; 
    for (int i=0;i<result.size();i++) {
        cout << result[i] <<" "; 
    }
    cout << endl;

    return 0;
}
