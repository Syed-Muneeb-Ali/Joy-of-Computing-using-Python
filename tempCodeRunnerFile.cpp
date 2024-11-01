#include <bits/stdc++.h>
using namespace std;

void binarySearch(int low, int high){
    int steps = 0;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        cout << "Is " << mid  << " your number: ";
        string got; cin >> got;
        
        if (got == "yes"){
            cout << "great I found your number in " << steps << " steps" << endl;
            break;
        }
        else{
            cout << "Is it less then: ";
            string less; cin >> less;
            if(less == "yes") high = mid-1;
            else low = mid+1;
            steps++;
        }
    }
}

// Driver code
int main(){
    binarySearch(1, 100000);    
}
